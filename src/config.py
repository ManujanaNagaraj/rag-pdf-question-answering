"""
PDF Extraction Module Configuration

This file contains all configuration parameters for the PDF text extraction module.
It centralizes settings to make the code more maintainable and configurable.
"""

# ==================== FILE HANDLING SETTINGS ====================

# Supported file extensions for PDF processing
SUPPORTED_EXTENSIONS = ['.pdf']

# Maximum file size in MB (default: 50MB to prevent memory issues)
MAX_FILE_SIZE_MB = 50

# ==================== EXTRACTION SETTINGS ====================

# Text encoding for extracted content
TEXT_ENCODING = 'utf-8'

# How to handle encoding errors: 'strict', 'ignore', or 'replace'
ERROR_HANDLING = 'replace'

# Whether to preserve line breaks in extracted text
PRESERVE_LINE_BREAKS = True

# Whether to remove extra whitespace from extracted text
REMOVE_EXTRA_WHITESPACE = True

# ==================== LOGGING SETTINGS ====================

# Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_LEVEL = 'INFO'

# Log format
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# ==================== METADATA SETTINGS ====================

# List of metadata fields to extract from PDFs
METADATA_FIELDS = [
    'title',
    'author',
    'subject',
    'creator',
    'producer',
    'creation_date',
    'modification_date'
]
