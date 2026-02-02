# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-02-02

### Added - Phase 1: PDF Text Extraction Module

#### Core Features
- **PDF Text Extraction**: Extract full text from PDF documents
- **Page-by-Page Extraction**: Get text separated by pages with metadata
- **PDF Metadata Extraction**: Retrieve document info (title, author, page count, etc.)
- **File Validation**: Check file existence, format, and size before processing
- **Error Handling**: Robust handling of encrypted, corrupted, and invalid PDFs

#### Configuration
- Centralized configuration system in `src/config.py`
- Configurable file size limits (default: 50MB)
- Configurable text processing options
- Logging configuration

#### Testing & Examples
- Comprehensive test suite with 4 test cases
- Sample PDF documents for testing
- Example scripts demonstrating usage
- PDF generation utility for creating test files

#### Documentation
- Main project README with architecture overview
- Module-specific documentation
- API reference with examples
- Contributing guidelines
- MIT License

#### Project Structure
- Clean folder organization (src/, tests/, data/, examples/, scripts/)
- Version control setup with Git
- GitHub repository integration

### Technical Details
- Python 3.8+ support
- PyPDF2 3.0.1 for PDF processing
- Type hints for better code quality
- Comprehensive docstrings

### Commits
- 11+ granular commits documenting development process
- Clear commit messages following best practices

---

## [Unreleased] - Future Phases

### Phase 2: Text Chunking (Planned)
- Semantic text chunking
- Chunk size configuration
- Context preservation
- Overlap management

### Phase 3: Embedding Generation (Planned)
- Embedding model integration
- Batch processing
- Vector generation

### Phase 4: Vector Database (Planned)
- ChromaDB or FAISS integration
- Similarity search
- Index management

### Phase 5: LLM Integration (Planned)
- OpenAI/HuggingFace integration
- RAG pipeline
- Hallucination prevention
- Prompt engineering

### Phase 6: System Integration (Planned)
- End-to-end pipeline
- CLI/API interface
- Web UI
- Performance optimization
