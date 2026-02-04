"""
Example: Using the PDF Extraction Module

This script demonstrates how to use all three main functions
of the PDF extraction module.
"""

import os
import sys

# Add parent directory to path to import src module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.pdf_extractor import (
    extract_text_from_pdf,
    extract_text_by_pages,
    get_pdf_metadata
)

def main():
    """Run examples for all extraction functions"""
    
    # Example PDF file
    pdf_file = "data/sample_pdfs/sample1.pdf"
    
    print("=" * 70)
    print("PDF EXTRACTION MODULE - EXAMPLES")
    print("=" * 70)
    
    # Example 1: Get metadata
    print("\n📊 EXAMPLE 1: Get PDF Metadata")
    print("-" * 70)
    metadata = get_pdf_metadata(pdf_file)
    print(f"File: {metadata['file_name']}")
    print(f"Pages: {metadata['page_count']}")
    print(f"Size: {metadata['file_size_mb']} MB")
    
    # Example 2: Extract all text
    print("\n📄 EXAMPLE 2: Extract All Text")
    print("-" * 70)
    full_text = extract_text_from_pdf(pdf_file)
    print(f"Total characters: {len(full_text)}")
    print(f"Total words: {len(full_text.split())}")
    print(f"\nFirst 300 characters:\n{full_text[:300]}...")
    
    # Example 3: Extract by pages
    print("\n📚 EXAMPLE 3: Extract Text by Pages")
    print("-" * 70)
    pages = extract_text_by_pages(pdf_file)
    for page in pages:
        print(f"Page {page['page_number']}: {page['char_count']} characters")
    
    print("\n" + "=" * 70)
    print("✅ All examples completed successfully!")
    print("=" * 70)

if __name__ == "__main__":
    main()
