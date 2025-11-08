"""Type exports for pypdfmake."""

# Re-export all types from submodules for convenience
from pypdfmake.types.base import (
    Size,
    PatternFill,
    Margins,
    Decoration,
    DecorationStyle,
    Alignment,
    Point,
    Position,
    Dash,
    LineStyle,
)
from pypdfmake.types.page import (
    PageSize,
    PageOrientation,
    PageBreak,
)
from pypdfmake.types.style import (
    Style,
    StyleReference,
    StyleDictionary,
)
from pypdfmake.types.callable import (
    DynamicRowSizeCallable,
    DynamicLayoutCallable,
    VerticalDynamicLayoutCallable,
    DynamicCellLayoutCallable,
    VerticalDynamicCellLayoutCallable,
    DynamicContentCallable,
    DynamicBackgroundCallable,
)
from pypdfmake.types.content import AnyContent, ContentTypes

__all__ = [
    # Base types
    "Size",
    "PatternFill",
    "Margins",
    "Decoration",
    "DecorationStyle",
    "Alignment",
    "Point",
    "Position",
    "Dash",
    "LineStyle",
    # Page types
    "PageSize",
    "PageOrientation",
    "PageBreak",
    # Style types
    "Style",
    "StyleReference",
    "StyleDictionary",
    # Callable types
    "DynamicRowSizeCallable",
    "DynamicLayoutCallable",
    "VerticalDynamicLayoutCallable",
    "DynamicCellLayoutCallable",
    "VerticalDynamicCellLayoutCallable",
    "DynamicContentCallable",
    "DynamicBackgroundCallable",
    # Content types
    "AnyContent",
    "ContentTypes",
]
