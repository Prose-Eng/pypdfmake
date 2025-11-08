# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Testing
- `poe test-no-watch` - Run tests once without file watching
- `poe test` - Run tests with file watching for development
- `poe test-cov` - Run tests with coverage reporting
- `poe test-cov-update` - Run tests with coverage and update README badge

### Version Management
- `poe patch` - Bump patch version (0.3.0 -> 0.3.1)
- `poe minor` - Bump minor version (0.3.0 -> 0.4.0)
- `poe major` - Bump major version (0.3.0 -> 1.0.0)
- `poe push_tags` - Push version tags to remote

### Coverage
- `poe coverage-report` - Display coverage report
- `poe coverage-html` - Generate HTML coverage report in `htmlcov/`

## Project Architecture

PyPDFMake is a Python library that generates pdfmake document definitions using Pydantic models. It provides type-safe creation of PDF documents by translating Python objects to JSON that can be consumed by the pdfmake JavaScript library.

### Core Architecture

The library is organized into several key modules:

1. **Types Module** (`src/pypdfmake/types/`): Core type definitions and base classes
   - `base.py`: Basic types like Size, Margins, Alignment, Point, Position
   - `page.py`: Page-related types (PageSize, PageOrientation, PageBreak)  
   - `style.py`: Style definitions and references
   - `callable.py`: Dynamic callable types for complex layouts

2. **Content Module** (`src/pypdfmake/content/`): Content element models
   - `base.py`: ContentBase and ContentLink base classes
   - `text.py`: Text content elements
   - `layout.py`: Layout containers (ContentColumns, ContentStack)
   - `lists.py`: Ordered and unordered lists
   - `table.py`: Table structures with complex layout support
   - `image.py`: Image and SVG content
   - `canvas.py`: Vector graphics elements
   - `qr.py`: QR code generation
   - `references.py`: Page/text references and table of contents

3. **Document Module** (`src/pypdfmake/document/`): Document-level definitions
   - `definition.py`: Main TDocumentDefinitions class and content unions
   - `info.py`: Document metadata and PDF settings
   - `fonts.py`: Font family definitions
   - `patterns.py`: Pattern and image dictionaries

### Key Design Patterns

- **Pydantic Models**: All classes inherit from `BaseModel` for validation and serialization
- **Union Types**: `AnyContent` and `ContentTypes` provide flexible content composition
- **Forward References**: Uses `from __future__ import annotations` for circular type references
- **Model Rebuilding**: All models are rebuilt at module end to resolve forward references
- **Style Inheritance**: ContentBase provides common styling and TOC properties

### Content System

The content system supports all pdfmake content types:
- Simple strings for basic text
- Structured content objects for complex formatting
- Layout containers for columns and stacks
- Tables with dynamic layouts and custom cell properties
- Vector graphics through canvas elements
- Images with positioning and sizing options
- Lists with custom markers and numbering
- References for page numbers and cross-references

### Style System

Styles follow a cascading pattern:
- `defaultStyle`: Applied to all elements
- Named styles in `styles` dictionary
- Inline styles on individual content elements
- Style references can be strings, Style objects, or lists for cascading

### Testing Structure

Tests are organized by content type and feature:
- `test_basic.py`: Basic document creation
- `test_styles*.py`: Style application and inheritance
- `test_tables.py`: Table layouts and cell properties
- `test_lists.py`: List formatting and markers
- `test_columns.py`: Column layouts
- `test_images.py`: Image positioning and sizing
- `test_margin.py`: Margin calculations

Each test typically creates a document definition, serializes to JSON, and compares against expected output stored in `tests/expected_outputs/`.

### Export Process

The library exports to JSON via Pydantic's `model_dump_json(exclude_none=True)` method. This creates clean JSON that matches pdfmake's expected format, with undefined/None values excluded.

## Development Notes

- Python 3.10+ required (uses modern union syntax with `|`)
- Heavy use of Literal types for string enums
- Pydantic v2 validation and serialization
- 100% test coverage maintained
- Uses `poethepoet` for task management instead of npm scripts