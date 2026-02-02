# PDF Text Extraction Module

## Overview

This module provides robust PDF text extraction capabilities for the RAG (Retrieval-Augmented Generation) Question Answering system. It uses PyPDF2 to extract text from PDF documents with proper error handling and validation.

## Features

- ✅ **Full Document Extraction**: Extract all text from a PDF in one call
- ✅ **Page-by-Page Extraction**: Get text separated by pages for granular processing
- ✅ **Metadata Extraction**: Retrieve PDF metadata (title, author, page count, etc.)
- ✅ **Robust Error Handling**: Handles corrupted, encrypted, and invalid files gracefully
- ✅ **Configurable**: Centralized configuration for all extraction settings
- ✅ **Well-Documented**: Comprehensive docstrings and beginner-friendly comments

## Installation

Install the required dependency:

```bash
pip install PyPDF2==3.0.1
```

## Usage

### 1. Extract All Text from a PDF

```python
from src.pdf_extractor import extract_text_from_pdf

# Extract all text
text = extract_text_from_pdf("path/to/document.pdf")
print(f"Extracted {len(text)} characters")
print(text[:500])  # Preview first 500 characters
```

### 2. Extract Text Page by Page

```python
from src.pdf_extractor import extract_text_by_pages

# Get text for each page
pages = extract_text_by_pages("path/to/document.pdf")

for page in pages:
    print(f"Page {page['page_number']}: {page['char_count']} characters")
    print(page['text'][:200])  # Preview first 200 chars
```

### 3. Get PDF Metadata

```python
from src.pdf_extractor import get_pdf_metadata

# Extract metadata
metadata = get_pdf_metadata("path/to/document.pdf")

print(f"Title: {metadata.get('title', 'N/A')}")
print(f"Author: {metadata.get('author', 'N/A')}")
print(f"Pages: {metadata['page_count']}")
print(f"File Size: {metadata['file_size_mb']} MB")
```

## API Reference

### `extract_text_from_pdf(file_path: str) -> str`

Extracts all text from a PDF file as a single string.

**Parameters:**
- `file_path` (str): Path to the PDF file

**Returns:**
- `str`: Extracted text from all pages

**Raises:**
- `FileNotFoundError`: If the PDF file doesn't exist
- `ValueError`: If the file is invalid, encrypted, or exceeds size limit
- `Exception`: For other PDF reading errors

---

### `extract_text_by_pages(file_path: str) -> List[Dict]`

Extracts text from a PDF with page-level granularity.

**Parameters:**
- `file_path` (str): Path to the PDF file

**Returns:**
- `List[Dict]`: List of dictionaries containing:
  - `page_number` (int): Page number (1-indexed)
  - `text` (str): Extracted text from that page
  - `char_count` (int): Number of characters on the page

**Raises:**
- Same as `extract_text_from_pdf`

---

### `get_pdf_metadata(file_path: str) -> Dict`

Extracts metadata from a PDF file.

**Parameters:**
- `file_path` (str): Path to the PDF file

**Returns:**
- `Dict`: Dictionary containing:
  - `file_name` (str): Name of the file
  - `file_path` (str): Absolute path to the file
  - `file_size_mb` (float): File size in megabytes
  - `page_count` (int): Number of pages
  - `is_encrypted` (bool): Whether the PDF is encrypted
  - `title` (str|None): PDF title
  - `author` (str|None): PDF author
  - Other metadata fields as available

**Raises:**
- Same as `extract_text_from_pdf`

## Configuration

All extraction settings are centralized in `src/config.py`:

```python
# Maximum file size (default: 50MB)
MAX_FILE_SIZE_MB = 50

# Text processing options
PRESERVE_LINE_BREAKS = True
REMOVE_EXTRA_WHITESPACE = True

# Error handling mode: 'strict', 'ignore', or 'replace'
ERROR_HANDLING = 'replace'
```

Modify these settings to customize the extraction behavior.

## Error Handling

The module provides comprehensive error handling:

| Error Type | Description | Solution |
|------------|-------------|----------|
| `FileNotFoundError` | PDF file doesn't exist | Check the file path |
| `ValueError` (size) | File exceeds max size | Increase `MAX_FILE_SIZE_MB` in config |
| `ValueError` (encrypted) | PDF is encrypted | Decrypt the PDF first |
| `ValueError` (type) | Not a PDF file | Ensure file has .pdf extension |

## Testing

Run the test suite to verify functionality:

```bash
python tests/test_extraction.py
```

This will test:
- ✅ Full text extraction
- ✅ Page-by-page extraction
- ✅ Metadata extraction
- ✅ Error handling

## Next Steps

This module is the first component of the RAG system. Future modules will include:

1. **Text Chunking**: Split extracted text into semantic chunks
2. **Embedding Generation**: Convert chunks into vector embeddings
3. **Vector Storage**: Store embeddings in a vector database
4. **Retrieval**: Find relevant chunks for user queries
5. **LLM Integration**: Generate answers using retrieved context

## Troubleshooting

### Issue: "Cannot extract text from encrypted PDF"
**Solution**: Use a PDF decryption tool or library to decrypt the PDF first.

### Issue: "Module 'PyPDF2' not found"
**Solution**: Install dependencies with `pip install -r requirements.txt`

### Issue: "Empty text extracted from PDF"
**Solution**: The PDF might be image-based (scanned). Consider using OCR tools like Tesseract.

## License

Part of the RAG PDF Question Answering System project.
