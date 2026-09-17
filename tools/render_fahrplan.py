"""Render the marked overview in FAHRPLAN.md as a single A4 page.

The Markdown is the source of truth. This renderer never starts model services
or reads private mail data. Requires reportlab and pypdf.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "FAHRPLAN.md"
OUTPUT = ROOT / "output" / "pdf" / "Bad-Wolf-Fahrplan.pdf"
INK = colors.HexColor("#18343D")
MUTED = colors.HexColor("#52666C")
ACCENT = colors.HexColor("#147A79")
PALE = colors.HexColor("#EDF5F4")


def inline(text: str) -> str:
    safe = html.escape(text)
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", safe)


def overview() -> list[str]:
    text = SOURCE.read_text(encoding="utf-8")
    start, end = "<!-- ONEPAGE_START -->", "<!-- ONEPAGE_END -->"
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError("Expected one overview block in FAHRPLAN.md")
    return text.split(start, 1)[1].split(end, 1)[0].strip().splitlines()


def fonts() -> tuple[str, str]:
    font_root = Path("C:/Windows/Fonts")
    if (font_root / "arial.ttf").exists() and (font_root / "arialbd.ttf").exists():
        pdfmetrics.registerFont(TTFont("Fahrplan", str(font_root / "arial.ttf")))
        pdfmetrics.registerFont(TTFont("Fahrplan-Bold", str(font_root / "arialbd.ttf")))
        pdfmetrics.registerFontFamily("Fahrplan", normal="Fahrplan", bold="Fahrplan-Bold")
        return "Fahrplan", "Fahrplan-Bold"
    return "Helvetica", "Helvetica-Bold"


def main() -> None:
    regular, bold = fonts()
    body = ParagraphStyle(
        "Body", fontName=regular, fontSize=9.4, leading=12.5,
        textColor=INK, spaceAfter=5.5, alignment=TA_LEFT,
    )
    heading = ParagraphStyle(
        "Heading", parent=body, fontName=bold, fontSize=11,
        leading=13.5, textColor=ACCENT, spaceBefore=8, spaceAfter=4,
        keepWithNext=True,
    )
    bullet = ParagraphStyle("Bullet", parent=body, leftIndent=9, firstLineIndent=-7)
    cell = ParagraphStyle("Cell", parent=body, fontSize=8.7, leading=11.2, spaceAfter=0)
    title = ParagraphStyle(
        "Title", parent=body, fontName=bold, fontSize=25, leading=29,
        spaceAfter=5,
    )
    subtitle = ParagraphStyle("Subtitle", parent=body, fontSize=9, textColor=MUTED, spaceAfter=13)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT), pagesize=A4, rightMargin=38, leftMargin=38,
        topMargin=33, bottomMargin=39,
        title="Bad Wolf - Fahrplan auf einem Blatt", author="Tudor / Codex",
        subject="Vereinbarte Richtung, geprüfter Stand und nächste Arbeitspakete",
    )
    story = [
        Paragraph("BAD WOLF", title),
        Paragraph("Unser Fahrplan  |  Stand 17.09.2026  |  Entscheidungen vor Umsetzung", subtitle),
    ]
    lines = overview()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line or line.startswith("## "):
            i += 1
            continue
        if line.startswith("### "):
            story.append(Paragraph(inline(line[4:]), heading))
        elif line.startswith("| "):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                row = [part.strip() for part in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r"[-: ]+", part) for part in row):
                    rows.append([Paragraph(inline(part), cell) for part in row])
                i += 1
            table = Table(rows, colWidths=[160, 211, A4[0] - 76 - 371], hAlign="LEFT")
            table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), PALE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LINEBELOW", (0, 0), (-1, 0), 0.8, ACCENT),
                ("LINEBELOW", (0, 1), (-1, -1), 0.3, colors.HexColor("#DDE6E7")),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]))
            story.append(table)
            story.append(Spacer(1, 3))
            continue
        elif line.startswith("- "):
            story.append(Paragraph("&#8226; " + inline(line[2:]), bullet))
        else:
            story.append(Paragraph(inline(line), body))
        i += 1

    def footer(canvas, _document):
        canvas.saveState()
        canvas.setStrokeColor(ACCENT)
        canvas.setLineWidth(0.6)
        canvas.line(38, 33, A4[0] - 38, 33)
        canvas.setFont(regular, 8)
        canvas.setFillColor(MUTED)
        canvas.drawString(38, 21, "Details, Abnahmen und Quellen: FAHRPLAN.md im Hauptrepo")
        canvas.drawRightString(A4[0] - 38, 21, str(_document.page))
        canvas.restoreState()

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    result = PdfReader(OUTPUT)
    if len(result.pages) != 1:
        raise ValueError(f"Overview must fit one page, got {len(result.pages)}")
    extracted = result.pages[0].extract_text()
    for expected in ("Grill-me", "Multi-Agent-Produktionsplattform", "4.194/4.201", "VoiceStudio", "12-GB", "Kundenaufträge"):
        if expected not in extracted:
            raise ValueError(f"Expected overview content missing: {expected}")
    print(f"Created and text-checked one-page PDF: {OUTPUT}")


if __name__ == "__main__":
    main()
