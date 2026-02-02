"""
PDF Text Extractor Module

This module provides functions to extract text from PDF documents.
It serves as the foundation for the RAG-based Question Answering system.

Main Functions:
- extract_text_from_pdf(file_path): Extract all text from a PDF
- extract_text_by_pages(file_path): Extract text page-by-page
- get_pdf_metadata(file_path): Get PDF metadata information

Author: RAG PDF QA System
Version: 0.1.0
"""

import os
import logging
from typing import List, Dict, Optional
from PyPDF2 import PdfReader

# Import configuration settings
from .config import (
    SUPPORTED_EXTENSIONS,
    MAX_FILE_SIZE_MB,
    TEXT_ENCODING,
    ERROR_HANDLING,
    PRESERVE_LINE_BREAKS,
    REMOVE_EXTRA_WHITESPACE,
    LOG_LEVEL,
    LOG_FORMAT,
    METADATA_FIELDS
)

# Configure logging
logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


def validate_pdf_file(file_path: str) -> bool:
    """
    Validate that the file exists, is a PDF, and meets size requirements.
    
    Args:
        file_path (str): Path to the PDF file
        
    Returns:
        bool: True if file is valid, raises exception otherwise
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file is not a PDF or exceeds size limit
    """
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Check file extension
    file_ext = os.path.splitext(file_path)[1].lower()
    if file_ext not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported file type: {file_ext}. Expected PDF file.")
    
    # Check file size
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
    if file_size_mb > MAX_FILE_SIZE_MB:
        raise ValueError(f"File size ({file_size_mb:.2f}MB) exceeds maximum allowed size ({MAX_FILE_SIZE_MB}MB)")
    
    logger.info(f"File validation passed: {file_path}")
    return True


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract all text content from a PDF file.
    
    This function reads a PDF file and extracts all text from all pages,
    combining them into a single string. Useful for processing the entire
    document at once.
    
    Args:
        file_path (str): Path to the PDF file
        
    Returns:
        str: Extracted text from all pages
        
    Raises:
        FileNotFoundError: If the PDF file doesn't exist
        ValueError: If the file is invalid or encrypted
        Exception: For other PDF reading errors
        
    Example:
        >>> text = extract_text_from_pdf("documents/sample.pdf")
        >>> print(f"Extracted {len(text)} characters")
    """
    try:
        # Validate the file first
        validate_pdf_file(file_path)
        
        # Open and read the PDF
        logger.info(f"Opening PDF file: {file_path}")
        reader = PdfReader(file_path)
        
        # Check if PDF is encrypted
        if reader.is_encrypted:
            logger.warning(f"PDF is encrypted: {file_path}")
            raise ValueError("Cannot extract text from encrypted PDF. Please decrypt first.")
        
        # Extract text from all pages
        num_pages = len(reader.pages)
        logger.info(f"PDF has {num_pages} pages")
        
        all_text = []
        for page_num, page in enumerate(reader.pages, start=1):
            logger.debug(f"Extracting text from page {page_num}/{num_pages}")
            page_text = page.extract_text()
            
            # Apply text processing based on config
            if REMOVE_EXTRA_WHITESPACE:
                page_text = ' '.join(page_text.split())
            
            all_text.append(page_text)
        
        # Join all pages with line break or space
        separator = '\n\n' if PRESERVE_LINE_BREAKS else ' '
        combined_text = separator.join(all_text)
        
        logger.info(f"Successfully extracted {len(combined_text)} characters from {num_pages} pages")
        return combined_text
        
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        raise
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        raise
    except Exception as e:
        logger.error(f"Error extracting text from PDF: {e}")
        raise Exception(f"Failed to extract text: {str(e)}")


def extract_text_by_pages(file_path: str) -> List[Dict[str, any]]:
    """
    Extract text from a PDF with page-level granularity.
    
    This function returns text separated by pages, which is useful for
    maintaining document structure and creating page-specific embeddings.
    
    Args:
        file_path (str): Path to the PDF file
        
    Returns:
        List[Dict]: List of dictionaries, each containing:
            - 'page_number': Page number (1-indexed)
            - 'text': Extracted text from that page
            - 'char_count': Number of characters on the page
            
    Example:
        >>> pages = extract_text_by_pages("documents/sample.pdf")
        >>> for page in pages:
        ...     print(f"Page {page['page_number']}: {page['char_count']} chars")
    """
    try:
        # Validate the file first
        validate_pdf_file(file_path)
        
        # Open and read the PDF
        logger.info(f"Opening PDF file for page-by-page extraction: {file_path}")
        reader = PdfReader(file_path)
        
        # Check if PDF is encrypted
        if reader.is_encrypted:
            logger.warning(f"PDF is encrypted: {file_path}")
            raise ValueError("Cannot extract text from encrypted PDF. Please decrypt first.")
        
        # Extract text page by page
        pages_data = []
        num_pages = len(reader.pages)
        
        for page_num, page in enumerate(reader.pages, start=1):
            logger.debug(f"Processing page {page_num}/{num_pages}")
            
            # Extract text from current page
            page_text = page.extract_text()
            
            # Apply text processing
            if REMOVE_EXTRA_WHITESPACE:
                page_text = ' '.join(page_text.split())
            
            # Create page data dictionary
            page_data = {
                'page_number': page_num,
                'text': page_text,
                'char_count': len(page_text)
            }
            
            pages_data.append(page_data)
        
        logger.info(f"Successfully extracted text from {num_pages} pages")
        return pages_data
        
    except (FileNotFoundError, ValueError) as e:
        logger.error(f"Error: {e}")
        raise
    except Exception as e:
        logger.error(f"Error extracting text by pages: {e}")
        raise Exception(f"Failed to extract text by pages: {str(e)}")


def get_pdf_metadata(file_path: str) -> Dict[str, any]:
    """
    Extract metadata information from a PDF file.
    
    Retrieves information like title, author, creation date, etc.
    Useful for document categorization and tracking.
    
    Args:
        file_path (str): Path to the PDF file
        
    Returns:
        Dict: Dictionary containing PDF metadata:
            - 'file_name': Name of the file
            - 'file_size_mb': File size in megabytes
            - 'page_count': Number of pages
            - 'title': PDF title (if available)
            - 'author': PDF author (if available)
            - 'subject': PDF subject (if available)
            - 'creator': PDF creator application (if available)
            - And other metadata fields defined in config
            
    Example:
        >>> metadata = get_pdf_metadata("documents/sample.pdf")
        >>> print(f"Title: {metadata['title']}")
        >>> print(f"Pages: {metadata['page_count']}")
    """
    try:
        # Validate the file first
        validate_pdf_file(file_path)
        
        # Open and read the PDF
        logger.info(f"Extracting metadata from: {file_path}")
        reader = PdfReader(file_path)
        
        # Get basic file information
        metadata = {
            'file_name': os.path.basename(file_path),
            'file_path': os.path.abspath(file_path),
            'file_size_mb': round(os.path.getsize(file_path) / (1024 * 1024), 2),
            'page_count': len(reader.pages),
            'is_encrypted': reader.is_encrypted
        }
        
        # Extract PDF metadata if available
        pdf_metadata = reader.metadata
        if pdf_metadata:
            for field in METADATA_FIELDS:
                # PyPDF2 uses different naming conventions
                field_key = f'/{field.title().replace("_", "")}'
                if field_key in pdf_metadata:
                    metadata[field] = pdf_metadata[field_key]
                else:
                    metadata[field] = None
        
        logger.info(f"Successfully extracted metadata: {metadata['page_count']} pages")
        return metadata
        
    except (FileNotFoundError, ValueError) as e:
        logger.error(f"Error: {e}")
        raise
    except Exception as e:
        logger.error(f"Error extracting metadata: {e}")
        raise Exception(f"Failed to extract metadata: {str(e)}")


# Example usage (for demonstration)
if __name__ == "__main__":
    print("PDF Text Extractor Module")
    print("=" * 50)
    print("\nThis module provides three main functions:")
    print("1. extract_text_from_pdf(file_path) - Extract all text")
    print("2. extract_text_by_pages(file_path) - Extract text per page")
    print("3. get_pdf_metadata(file_path) - Get PDF information")
    print("\nExample usage:")
    print(">>> from src.pdf_extractor import extract_text_from_pdf")
    print(">>> text = extract_text_from_pdf('data/sample_pdfs/sample1.pdf')")
    print(">>> print(text)")
