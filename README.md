# RAG PDF Question Answering System

A **Retrieval-Augmented Generation (RAG)** based Context-Aware Question Answering system for PDF documents built with Python.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-In%20Development-yellow.svg)]()

## 🎯 Project Overview

This system enables users to:
- 📄 Upload text-based PDF documents
- 🔍 Ask questions about the document content
- 💡 Receive accurate, context-aware answers
- ✅ Minimize LLM hallucinations through grounded retrieval

## ✨ Features

- **PDF Text Extraction**: Extract text from PDF documents with validation
- **Semantic Chunking**: Split text into meaningful chunks (Coming Soon)
- **Vector Embeddings**: Generate embeddings for semantic search (Coming Soon)
- **Vector Database**: Store and retrieve relevant chunks efficiently (Coming Soon)
- **LLM Integration**: Generate answers strictly based on retrieved context (Coming Soon)
- **Modular Design**: Clean, maintainable, and extensible codebase

## 🏗️ Architecture

```
┌──────────────┐
│  PDF Upload  │
└──────┬───────┘
       │
       ▼
┌──────────────────┐
│ Text Extraction  │  ✅ COMPLETE
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ Semantic Chunking│  🚧 Coming Soon
└──────┬───────────┘
       │
       ├──────────────────┐
       ▼                  ▼
┌─────────────┐    ┌──────────────┐
│  Embedding  │    │   Vector     │  🚧 Coming Soon
│ Generation  │───▶│   Database   │
└─────────────┘    └──────┬───────┘
                          │
                          ▼
                   ┌──────────────┐
          Query───▶│  Retrieval   │  🚧 Coming Soon
                   └──────┬───────┘
                          │
                          ▼
                   ┌──────────────┐
                   │     LLM      │  🚧 Coming Soon
                   │    Answer    │
                   └──────────────┘
```

## 📁 Project Structure

```
RAG/
├── src/                          # Source code
│   ├── __init__.py              # Package initialization
│   ├── config.py                # Configuration settings
│   ├── pdf_extractor.py         # PDF text extraction ✅
│   └── README.md                # Module documentation
├── tests/                        # Test suite
│   ├── __init__.py
│   └── test_extraction.py       # PDF extraction tests
├── data/                         # Data directory
│   └── sample_pdfs/             # Sample PDF files
│       ├── sample1.pdf
│       └── sample2.pdf
├── scripts/                      # Utility scripts
│   └── generate_sample_pdfs.py  # PDF generation script
├── requirements.txt              # Python dependencies
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/ManujanaNagaraj/rag-pdf-question-answering.git
cd rag-pdf-question-answering
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

### Usage

#### Extract Text from PDF

```python
from src.pdf_extractor import extract_text_from_pdf

# Extract all text from a PDF
text = extract_text_from_pdf("data/sample_pdfs/sample1.pdf")
print(f"Extracted {len(text)} characters")
print(text[:500])  # Preview
```

#### Extract Text Page by Page

```python
from src.pdf_extractor import extract_text_by_pages

# Get text for each page
pages = extract_text_by_pages("data/sample_pdfs/sample1.pdf")

for page in pages:
    print(f"Page {page['page_number']}: {page['char_count']} chars")
```

#### Get PDF Metadata

```python
from src.pdf_extractor import get_pdf_metadata

# Get PDF information
metadata = get_pdf_metadata("data/sample_pdfs/sample1.pdf")
print(f"Title: {metadata.get('title', 'N/A')}")
print(f"Pages: {metadata['page_count']}")
```

### Running Tests

```bash
python tests/test_extraction.py
```

Expected output:
```
🧪🧪🧪🧪🧪...
  PDF EXTRACTION MODULE - TEST SUITE
...
✅ All tests passed successfully!
```

## 📚 Module Documentation

For detailed API documentation and usage examples, see:
- [PDF Extraction Module Documentation](src/README.md)

## 🗓️ Development Roadmap

### Phase 1: PDF Text Extraction ✅ COMPLETE
- [x] PDF text extraction
- [x] Page-by-page extraction
- [x] Metadata extraction
- [x] Error handling
- [x] Test suite
- [x] Documentation

### Phase 2: Text Chunking 🚧 Next
- [ ] Implement semantic chunking
- [ ] Add chunk size configuration
- [ ] Preserve context across chunks
- [ ] Add overlap for better retrieval

### Phase 3: Embedding Generation 🔜 Future
- [ ] Select embedding model (e.g., all-MiniLM-L6-v2)
- [ ] Generate embeddings for chunks
- [ ] Batch processing for efficiency

### Phase 4: Vector Database 🔜 Future
- [ ] Set up ChromaDB or FAISS
- [ ] Store embeddings with metadata
- [ ] Implement similarity search

### Phase 5: LLM Integration 🔜 Future
- [ ] Integrate OpenAI or HuggingFace LLM
- [ ] Design prompt templates
- [ ] Implement RAG pipeline
- [ ] Add hallucination prevention

### Phase 6: System Integration 🔜 Future
- [ ] Build end-to-end pipeline
- [ ] Create CLI/API interface
- [ ] Add example notebooks
- [ ] Performance optimization

## 🛠️ Technologies Used

- **Python 3.8+**: Core programming language
- **PyPDF2**: PDF text extraction
- **Future**: LangChain, ChromaDB/FAISS, Sentence Transformers, OpenAI/HuggingFace

## 📖 How It Works

### Current Implementation (Phase 1)

1. **PDF Validation**: Checks file existence, format, and size
2. **Text Extraction**: Extracts text using PyPDF2
3. **Processing**: Cleans and formats extracted text
4. **Metadata**: Retrieves document information

### Future Implementation (Phases 2-6)

1. **Chunking**: Split text into semantic chunks
2. **Embedding**: Convert chunks to vectors
3. **Storage**: Store in vector database
4. **Retrieval**: Find relevant chunks for queries
5. **Generation**: Generate answers using LLM with retrieved context

## 🤝 Contributing

This is an educational project. Contributions, suggestions, and feedback are welcome!

## 📝 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Manujana Nagaraj**
- GitHub: [@ManujanaNagaraj](https://github.com/ManujanaNagaraj)

## 🙏 Acknowledgments

- Built as part of learning RAG systems and AI engineering
- Inspired by modern LLM-based question answering systems

---

**Note**: This project is under active development. The PDF extraction module is complete. Future modules will be added incrementally with comprehensive documentation.
