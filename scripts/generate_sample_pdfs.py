"""
Script to generate sample PDF files for testing

This script creates sample PDFs from text files using reportlab.
Run this once to generate the test PDFs.
"""

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import os

def create_pdf_from_text(text_file, pdf_file, title="Sample PDF"):
    """Create a PDF from a text file"""
    
    # Read the text file
    with open(text_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create PDF
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    
    # Add title style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=30
    )
    
    # Split content into paragraphs
    paragraphs = content.split('\n\n')
    
    for para in paragraphs:
        if para.strip():
            # Check if it's a title or heading
            if para.strip().startswith('Page '):
                # Add page break before new pages (except first)
                if story:
                    story.append(PageBreak())
                story.append(Paragraph(para.strip(), styles['Heading1']))
            elif any(para.strip().startswith(prefix) for prefix in ['Sample PDF', 'Introduction to', 'Machine Learning']):
                story.append(Paragraph(para.strip(), title_style))
            else:
                story.append(Paragraph(para.strip(), styles['BodyText']))
            story.append(Spacer(1, 0.2*inch))
    
    # Build PDF
    doc.build(story)
    print(f"✅ Created: {pdf_file}")

def main():
    """Generate all sample PDFs"""
    print("Generating sample PDF files...")
    print("=" * 50)
    
    # Define input/output pairs
    samples = [
        ("data/sample_pdfs/sample1.txt", "data/sample_pdfs/sample1.pdf"),
        ("data/sample_pdfs/sample2.txt", "data/sample_pdfs/sample2.pdf")
    ]
    
    # Generate each PDF
    for text_file, pdf_file in samples:
        if os.path.exists(text_file):
            create_pdf_from_text(text_file, pdf_file)
        else:
            print(f"⚠️  Text file not found: {text_file}")
    
    print("=" * 50)
    print("✅ PDF generation complete!")

if __name__ == "__main__":
    main()
