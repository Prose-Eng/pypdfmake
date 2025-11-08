"""Pypdfmake - Python types for pdfmake document generation."""

# Key document and content types
from pypdfmake.document import (
    TDocumentDefinitions,
    TDocumentInformation,
    TFontFamilyTypes,
    AnyContent,
    ContentTypes,
)
from pypdfmake.content import (
    ContentText,
    ContentColumns,
    ContentStack,
    ContentUnorderedList,
    ContentOrderedList,
    ContentTable,
    ContentImage,
    ContentSvg,
    ContentQr,
    ContentCanvas,
    ContentBase,
    ContentLink,
    # Table related
    CustomTableLayout,
    PredefinedTableLayout,
    TableLayout,
    TableCell,
    Table,
    # References
    TableOfContent,
    # List elements
    OrderedListElement,
    UnorderedListElement,
)

# Core style and page types
from pypdfmake.types import (
    Style,
    StyleReference,
    StyleDictionary,
    Margins,
    Alignment,
    PageSize,
    PageOrientation,
    PageBreak,
    Size,
    Point,
    Position,
)

__all__ = [
    # Document types
    "TDocumentDefinitions",
    "TDocumentInformation", 
    "TFontFamilyTypes",
    "AnyContent",
    "ContentTypes",
    # Content elements
    "ContentText",
    "ContentColumns",
    "ContentStack",
    "ContentUnorderedList",
    "ContentOrderedList",
    "ContentTable",
    "ContentImage",
    "ContentSvg",
    "ContentQr",
    "ContentCanvas",
    "ContentBase",
    "ContentLink",
    # Table related
    "CustomTableLayout",
    "PredefinedTableLayout",
    "TableLayout",
    "TableCell",
    "Table",
    # References
    "TableOfContent",
    # List elements
    "OrderedListElement",
    "UnorderedListElement",
    # Style and page types
    "Style",
    "StyleReference", 
    "StyleDictionary",
    "Margins",
    "Alignment",
    "PageSize",
    "PageOrientation",
    "PageBreak",
    "Size",
    "Point",
    "Position",
]
