"""
Interview Report PDF Generator using ReportLab.
Produces a clean, professional scorecard for candidates.
"""

import io
from datetime import datetime
from typing import List, Dict, Any

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

def generate_pdf_report(
    candidate_name: str,
    role: str,
    difficulty: str,
    total_score: int,
    max_score: int,
    qa_history: List[Dict[str, Any]]
) -> bytes:
    """Build and return a professional PDF report in bytes."""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=colors.HexColor('#1E3A8A'),
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        textColor=colors.HexColor('#4B5563'),
        spaceAfter=15
    )
    
    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#1F2937'),
        spaceBefore=12,
        spaceAfter=8
    )
    
    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#374151')
    )
    
    bold_body = ParagraphStyle(
        'BoldBody',
        parent=body_style,
        fontName='Helvetica-Bold',
        textColor=colors.HexColor('#111827')
    )
    
    percentage = (total_score / max_score * 100) if max_score > 0 else 0
    if percentage >= 80:
        verdict = "EXCELLENT - Highly Recommended"
        verdict_color = colors.HexColor('#059669')
    elif percentage >= 60:
        verdict = "PROFICIENT - Good Working Knowledge"
        verdict_color = colors.HexColor('#D97706')
    else:
        verdict = "DEVELOPING - Recommended for Further Practice"
        verdict_color = colors.HexColor('#DC2626')
        
    elements = []
    
    # 1. Header
    elements.append(Paragraph("AI Interview Simulator — Scorecard", title_style))
    current_time = datetime.now().strftime("%B %d, %Y - %I:%M %p")
    elements.append(Paragraph(f"Candidate Assessment Report &bull; Generated on {current_time}", subtitle_style))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#2563EB'), spaceAfter=15))
    
    # 2. Executive Summary Table
    summary_data = [
        [
            Paragraph("<b>Candidate Name:</b>", bold_body), Paragraph(candidate_name, body_style),
            Paragraph("<b>Target Role:</b>", bold_body), Paragraph(role, body_style)
        ],
        [
            Paragraph("<b>Difficulty Level:</b>", bold_body), Paragraph(difficulty, body_style),
            Paragraph("<b>Questions Answered:</b>", bold_body), Paragraph(f"{len(qa_history)} Questions", body_style)
        ],
        [
            Paragraph("<b>Total Score:</b>", bold_body), Paragraph(f"<b>{total_score} / {max_score} ({percentage:.1f}%)</b>", bold_body),
            Paragraph("<b>Performance Verdict:</b>", bold_body), Paragraph(f"<b>{verdict}</b>", ParagraphStyle('V', parent=body_style, textColor=verdict_color, fontName='Helvetica-Bold'))
        ]
    ]
    
    summary_table = Table(summary_data, colWidths=[120, 140, 120, 150])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F8FAFC')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#E2E8F0')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    elements.append(summary_table)
    elements.append(Spacer(1, 15))
    
    # 3. Question-by-Question Breakdown
    elements.append(Paragraph("Question Evaluation Breakdown", section_heading))
    
    for idx, item in enumerate(qa_history, 1):
        q_text = item.get("question", "N/A")
        ans_text = item.get("answer", "N/A")
        eval_dict = item.get("evaluation", {})
        score_val = eval_dict.get("score", 0)
        strengths = eval_dict.get("strengths", "Good effort.")
        improvements = eval_dict.get("improvements", "Continue practicing.")
        ideal = eval_dict.get("ideal_answer", "N/A")
        
        q_block = [
            [
                Paragraph(f"<b>Q{idx}: {q_text}</b>", ParagraphStyle('QStyle', parent=bold_body, textColor=colors.HexColor('#1E40AF'))),
                Paragraph(f"<b>Score: {score_val}/10</b>", ParagraphStyle('ScoreCol', parent=bold_body, alignment=2, textColor=colors.HexColor('#2563EB')))
            ],
            [
                Paragraph(f"<b>Candidate Answer:</b> {ans_text}", body_style),
                Paragraph("", body_style)
            ],
            [
                Paragraph(f"<b>Key Strengths:</b> {strengths}", ParagraphStyle('Str', parent=body_style, textColor=colors.HexColor('#065F46'))),
                Paragraph("", body_style)
            ],
            [
                Paragraph(f"<b>Areas for Growth:</b> {improvements}", ParagraphStyle('Imp', parent=body_style, textColor=colors.HexColor('#9A3412'))),
                Paragraph("", body_style)
            ],
            [
                Paragraph(f"<b>Ideal Reference Answer:</b> {ideal}", ParagraphStyle('Ide', parent=body_style, textColor=colors.HexColor('#374151'))),
                Paragraph("", body_style)
            ]
        ]
        
        table = Table(q_block, colWidths=[420, 110])
        table.setStyle(TableStyle([
            ('SPAN', (0, 1), (1, 1)),
            ('SPAN', (0, 2), (1, 2)),
            ('SPAN', (0, 3), (1, 3)),
            ('SPAN', (0, 4), (1, 4)),
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#FAFAFA')),
            ('BOX', (0, 0), (-1, -1), 0.75, colors.HexColor('#CBD5E1')),
            ('LINEBELOW', (0, 0), (-1, 0), 0.5, colors.HexColor('#CBD5E1')),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ]))
        elements.append(table)
        elements.append(Spacer(1, 10))
        
    elements.append(Spacer(1, 10))
    elements.append(Paragraph("<i>End of Report &bull; AI Interview Simulator &bull; https://github.com/aizazahmad736/AI-Interview-Simulator</i>", ParagraphStyle('F', parent=body_style, alignment=1, textColor=colors.HexColor('#9CA3AF'))))
    
    doc.build(elements)
    pdf_data = buffer.getvalue()
    buffer.close()
    return pdf_data
