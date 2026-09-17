#!/usr/bin/env node
/**
 * fix-optional-deps.mjs — repariert fehlende optionalDependencies.
 *
 * Warum: `npm ci` lässt optionalDependencies je nach Plattform/Registry still
 * aus (Native-Prebuilds, overrides-Konflikte). Ohne z. B.
 * `@huggingface/transformers` bricht der Dev-Server schon beim Kompilieren
 * der Instrumentation ab:
 *   Module not found: Can't resolve '@huggingface/transformers'
 *
 * Ablauf (idempotent — nur fehlende Pakete werden angefasst):
 *   1. Fehlende optionale Pakete normal via `npm install --no-save` nachziehen.
 *   2. Was npm weiterhin verweigert (z. B. overrides-Kandidaten wie
 *      onnxruntime-node), wird über `npm pack` + tar-Entpacken direkt nach
 *      node_modules/ gelegt (tar ist auf Windows 10+, Linux und macOS dabei).
 *   3. Fehlende transitive Abhängigkeiten paketierter Module noch einmal
 *      normal nachziehen.
 *
 * keytar ist bewusst NICHT fatal: ohne native Build-Tools bleibt es weg,
 * der Code hat dafür Laufzeit-Fallbacks (Keychain optional).
 *
 * Aufruf:  node scripts/setup/fix-optional-deps.mjs
 */
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..");
const NM = path.join(ROOT, "node_modules");
const pkg = JSON.parse(fs.readFileSync(path.join(ROOT, "package.json"), "utf8"));
const optional = Object.entries(pkg.optionalDependencies || {});

const isWin = process.platform === "win32";
const run = (cmd, args, cwd) =>
  spawnSync(cmd, args, { cwd, stdio: "pipe", encoding: "utf8", shell: isWin });

const nmPath = (name) => path.join(NM, ...name.split("/"));
const present = (name) => {
  try {
    return fs.existsSync(path.join(nmPath(name), "package.json"));
  } catch {
    return false;
  }
};

let missing = optional.filter(([name]) => !present(name));
if (!missing.length) {
  console.log("[fix-optional-deps] alle optionalen Pakete vorhanden — nichts zu tun.");
  process.exit(0);
}
console.log(
  `[fix-optional-deps] ${missing.length} fehlend: ` +
    missing.map(([n, v]) => `${n}@${v}`).join(", ")
);

if (!fs.existsSync(NM)) {
  console.error("[fix-optional-deps] node_modules fehlt — zuerst `npm ci` ausführen.");
  process.exit(1);
}

// ── Schritt 1: normaler Nachzug über npm ────────────────────────────
const step1 = missing;
const r1 = run("npm", [
  "install", "--no-save", "--no-audit", "--no-fund",
  ...step1.map(([n, v]) => `${n}@${v}`),
], ROOT);
if (r1.status !== 0) {
  console.warn("[fix-optional-deps] npm install teilweise fehlgeschlagen — pack-Fallback folgt.");
}

const stillMissing = () => optional.filter(([name]) => !present(name));

// ── Schritt 2: npm pack + tar für alles, was weiterhin fehlt ────────
const packInstall = (name, version) => {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "omniroute-optdep-"));
  try {
    const r = run("npm", ["pack", `${name}@${version}`, "--silent"], tmp);
    if (r.status !== 0) return false;
    const tgz = fs.readdirSync(tmp).find((f) => f.endsWith(".tgz"));
    if (!tgz) return false;
    const dest = nmPath(name);
    const parent = path.dirname(dest);
    fs.mkdirSync(parent, { recursive: true });
    const staging = path.join(tmp, "x");
    fs.mkdirSync(staging, { recursive: true });
    const ex = run("tar", ["-xzf", path.join(tmp, tgz), "-C", staging], tmp);
    if (ex.status !== 0) return false;
    fs.rmSync(dest, { recursive: true, force: true });
    fs.renameSync(path.join(staging, "package"), dest);
    return present(name);
  } finally {
    fs.rmSync(tmp, { recursive: true, force: true });
  }
};

for (const [name, version] of stillMissing()) {
  if (name === "keytar") {
    console.warn(`[fix-optional-deps] keytar übersprungen (optional, braucht native Build-Tools — Fallback aktiv).`);
    continue;
  }
  console.log(`[fix-optional-deps] ${name}: npm pack + entpacken …`);
  if (!packInstall(name, version)) {
    console.warn(`[fix-optional-deps] ${name}: konnte nicht installiert werden.`);
  }
}

// ── Schritt 3: transitive Abhängigkeiten der paketierten Module ─────
const transitives = new Set();
for (const [name] of optional) {
  const pj = path.join(nmPath(name), "package.json");
  if (!fs.existsSync(pj)) continue;
  try {
    const meta = JSON.parse(fs.readFileSync(pj, "utf8"));
    for (const dep of Object.keys(meta.dependencies || {})) {
      if (!present(dep)) transitives.add(dep);
    }
  } catch {
    /* defekte package.json ignorieren */
  }
}
if (transitives.size) {
  console.log(`[fix-optional-deps] transitive nachziehen: ${[...transitives].join(", ")}`);
  run("npm", ["install", "--no-save", "--no-audit", "--no-fund", ...transitives], ROOT);
}

// ── Abschlussbericht ─────────────────────────────────────────────────
const finalMissing = stillMissing().map(([n]) => n).filter((n) => n !== "keytar");
const fixed = optional.map(([n]) => n).filter((n) => present(n));
console.log(
  `[fix-optional-deps] vorhanden: ${fixed.length}/${optional.length}` +
    (fixed.length ? ` (${fixed.join(", ")})` : "")
);
if (finalMissing.length) {
  console.error(`[fix-optional-deps] FEHLT weiterhin: ${finalMissing.join(", ")}`);
  process.exit(1);
}
console.log("[fix-optional-deps] fertig.");
