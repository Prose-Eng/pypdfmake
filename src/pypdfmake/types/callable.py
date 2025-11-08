"""Callable type definitions for pypdfmake."""

from __future__ import annotations
from typing import Literal, Callable, Union, Any

# Using forward references to avoid circular imports
from pypdfmake.types.content import AnyContent
from pypdfmake.types.page import ContextPageSize

ContentTableRef = "ContentTable"  # Internal type alias, not for direct user use.

DynamicRowSizeCallable = Callable[[int], float | Literal["auto"]]
"""
A callable that dynamically determines row height in a table.
It receives:
- `rowIndex`: The 0-based index of the row.
Should return a height in points or 'auto'.
"""

DynamicLayoutCallable = Callable[[int, ContentTableRef], "Any | None"]
"""
A callable for dynamically determining horizontal table layout properties (lines, padding).
It receives:
- `index`: The 0-based index of the line or column.
- `node`: The `ContentTable` node itself.
Should return a value appropriate for the property (e.g., line width, padding value).
"""

VerticalDynamicLayoutCallable = Callable[[int, ContentTableRef], "Any | None"]
"""
A callable for dynamically determining vertical table layout properties (lines, padding).
It receives:
- `index`: The 0-based index of the line or row.
- `node`: The `ContentTable` node itself.
Should return a value appropriate for the property (e.g., line width, padding value).
"""

DynamicCellLayoutCallable = Callable[[int, ContentTableRef, int], "Any | None"]
"""
A callable for dynamically determining table cell layout properties (padding, fill color) for horizontal context.
It receives:
- `rowIndex`: The 0-based index of the row.
- `node`: The `ContentTable` node itself.
- `columnIndex`: The 0-based index of the column.
Should return a value appropriate for the property (e.g., padding value, color string).
"""

VerticalDynamicCellLayoutCallable = Callable[[int, ContentTableRef, int], "Any | None"]
"""
A callable for dynamically determining table cell layout properties (padding, fill color) for vertical context.
It receives:
- `columnIndex`: The 0-based index of the column.
- `node`: The `ContentTable` node itself.
- `rowIndex`: The 0-based index of the row.
Should return a value appropriate for the property (e.g., padding value, color string).
"""

DynamicContentCallable = Callable[
    [int, int, ContextPageSize], Union[AnyContent, list[AnyContent], None]
]
"""
A callable that dynamically generates content for elements like header, footer, or the main document body.
It receives:
- `currentPage`: The current page number (1-based).
- `pageCount`: The total number of pages in the document.
- `pageSize`: A `ContextPageSize` object with `width` and `height` of the current page.
Should return a single content element, a list of content elements, a string, or None.
"""

DynamicBackgroundCallable = Callable[
    [int, ContextPageSize], Union[AnyContent, list[AnyContent], None]
]
"""
A callable that dynamically generates background content for each page.
It receives:
- `currentPage`: The current page number (1-based).
- `pageSize`: A `ContextPageSize` object with `width` and `height` of the current page.
Should return a single content element, a list of content elements, a string, or None for the background.
"""
