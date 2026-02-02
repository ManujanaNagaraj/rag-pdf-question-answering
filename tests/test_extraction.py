"""
Test Script for PDF Extraction Module

This script tests the functionality of the PDF extraction module.
It provides simple tests to verify that:
1. Text extraction works correctly
2. Page-by-page extraction works
3. Metadata extraction works
4. Error handling works properly

Run this script after installing dependencies:
    python tests/test_extraction.py
"""

import os
import sys

# Add parent directory to path to import src module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.pdf_extractor import (
    extract_text_from_pdf,
    extract_text_by_pages,
    get_pdf_metadata,
    validate_pdf_file
)


def print_header(title):
    """Print a formatted header for test sections"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def test_metadata_extraction():
    """Test PDF metadata extraction"""
    print_header("TEST 1: PDF Metadata Extraction")
    
    sample_pdf = "data/sample_pdfs/sample1.pdf"
    
    try:
        print(f"\n📄 Testing metadata extraction from: {sample_pdf}")
        metadata = get_pdf_metadata(sample_pdf)
        
        print("\n✅ Metadata extracted successfully!")
        print(f"\n📊 PDF Information:")
        print(f"   - File Name: {metadata['file_name']}")
        print(f"   - File Size: {metadata['file_size_mb']} MB")
        print(f"   - Page Count: {metadata['page_count']}")
        print(f"   - Is Encrypted: {metadata['is_encrypted']}")
        
        if metadata.get('title'):
            print(f"   - Title: {metadata['title']}")
        if metadata.get('author'):
            print(f"   - Author: {metadata['author']}")
            
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False


def test_full_text_extraction():
    """Test extracting all text from PDF"""
    print_header("TEST 2: Full Text Extraction")
    
    sample_pdf = "data/sample_pdfs/sample1.pdf"
    
    try:
        print(f"\n📄 Extracting all text from: {sample_pdf}")
        text = extract_text_from_pdf(sample_pdf)
        
        print("\n✅ Text extracted successfully!")
        print(f"\n📝 Extraction Results:")
        print(f"   - Total characters: {len(text)}")
        print(f"   - Total words (approx): {len(text.split())}")
        
        # Show first 200 characters as preview
        print(f"\n📖 Text Preview (first 200 chars):")
        print(f"   {text[:200]}...")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False


def test_page_by_page_extraction():
    """Test extracting text page by page"""
    print_header("TEST 3: Page-by-Page Extraction")
    
    sample_pdf = "data/sample_pdfs/sample2.pdf"
    
    try:
        print(f"\n📄 Extracting text page-by-page from: {sample_pdf}")
        pages = extract_text_by_pages(sample_pdf)
        
        print("\n✅ Page-by-page extraction successful!")
        print(f"\n📚 Page Details:")
        
        for page in pages:
            print(f"   - Page {page['page_number']}: {page['char_count']} characters")
        
        # Show preview of first page
        if pages:
            print(f"\n📖 First Page Preview:")
            print(f"   {pages[0]['text'][:150]}...")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False


def test_error_handling():
    """Test error handling for invalid files"""
    print_header("TEST 4: Error Handling")
    
    print("\n🧪 Testing error handling with invalid file...")
    
    try:
        # Test with non-existent file
        extract_text_from_pdf("nonexistent.pdf")
        print("❌ Should have raised FileNotFoundError")
        return False
        
    except FileNotFoundError:
        print("✅ Correctly raised FileNotFoundError for missing file")
        return True
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


def run_all_tests():
    """Run all tests and display summary"""
    print("\n" + "🧪" * 35)
    print("  PDF EXTRACTION MODULE - TEST SUITE")
    print("🧪" * 35)
    
    # Check if sample PDFs exist
    sample_dir = "data/sample_pdfs"
    if not os.path.exists(sample_dir):
        print(f"\n⚠️  Warning: Sample PDF directory not found: {sample_dir}")
        print("   Please create sample PDFs first.")
        return
    
    # Run all tests
    results = []
    results.append(("Metadata Extraction", test_metadata_extraction()))
    results.append(("Full Text Extraction", test_full_text_extraction()))
    results.append(("Page-by-Page Extraction", test_page_by_page_extraction()))
    results.append(("Error Handling", test_error_handling()))
    
    # Print summary
    print_header("TEST SUMMARY")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"\n📊 Results: {passed}/{total} tests passed\n")
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"   {status} - {test_name}")
    
    if passed == total:
        print("\n🎉 All tests passed successfully!")
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please check the errors above.")
    
    print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    run_all_tests()
