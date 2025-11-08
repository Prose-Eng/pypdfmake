"""Page-related type definitions for pypdfmake."""

from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field

# PageSize related types
PredefinedPageSize = Literal[
    "4A0",
    "2A0",
    "A0",
    "A1",
    "A2",
    "A3",
    "A4",
    "A5",
    "A6",
    "A7",
    "A8",
    "A9",
    "A10",
    "B0",
    "B1",
    "B2",
    "B3",
    "B4",
    "B5",
    "B6",
    "B7",
    "B8",
    "B9",
    "B10",
    "C0",
    "C1",
    "C2",
    "C3",
    "C4",
    "C5",
    "C6",
    "C7",
    "C8",
    "C9",
    "C10",
    "RA0",
    "RA1",
    "RA2",
    "RA3",
    "RA4",
    "SRA0",
    "SRA1",
    "SRA2",
    "SRA3",
    "SRA4",
    "EXECUTIVE",
    "FOLIO",
    "LEGAL",
    "LETTER",
    "TABLOID",
]
"""Standard predefined page sizes for PDF documents."""


class CustomPageSize(BaseModel):
    """Defines a custom page size with specific width and height."""

    width: float = Field(description="The width of the page in points.")
    height: float = Field(description="The height of the page in points.")


PageSize = PredefinedPageSize | CustomPageSize
"""Represents the size of a page, either a predefined string (e.g., 'A4') or a CustomPageSize object."""

PageOrientation = Literal["portrait", "landscape"]
"""Defines the orientation of a page: 'portrait' or 'landscape'."""

PageBreak = Literal[
    "before", "beforeEven", "beforeOdd", "after", "afterEven", "afterOdd"
]
"""Specifies how a page break should occur relative to content (e.g., 'before' an element, 'afterOdd' page)."""


class ContextPageSize(BaseModel):
    """Represents the current page size context, typically passed to dynamic content functions."""

    width: float = Field(description="The width of the current page in points.")
    height: float = Field(description="The height of the current page in points.")
