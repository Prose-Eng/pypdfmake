"""Basic type definitions for pypdfmake."""

from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field

Size = float | Literal["auto", "*"] | str
"""
Represents a size value.
Can be:
- A number (in points).
- 'auto' (content-dependent size).
- '*' (star sizing, for proportional distribution of space, e.g., in table columns).
- A string percentage (e.g., "50%").
"""

PatternFill = tuple[str, str]
"""Defines a pattern fill with foreground and background colors: `[<foregroundColor>, <backgroundColor>]`."""

Margins = float | list[float]
"""
Represents margins.
Can be:
- A single number for all sides (e.g., `40`).
- A list of two numbers `[horizontal, vertical]` (e.g., `[20, 40]`).
- A list of four numbers `[left, top, right, bottom]` (e.g., `[10, 20, 10, 20]`).
"""

Decoration = Literal["underline", "strike", "overline"]
"""Text decoration type."""

DecorationStyle = Literal["dashed", "dotted", "double", "wavy"]
"""Style of the text decoration (e.g., 'dashed' underline)."""

Alignment = Literal["left", "right", "justify", "center"]
"""Text alignment options."""

Point = tuple[float, float]
"""Represents a 2D point as a tuple (x, y) in points, used in canvas elements."""


class Position(BaseModel):
    """Represents a 2D position with x and y coordinates."""

    x: float = Field(description="The x-coordinate in points.")
    y: float = Field(description="The y-coordinate in points.")


class Dash(BaseModel):
    """Defines a dash pattern for lines, used in canvas or borders."""

    length: float = Field(description="Length of the dash in points.")
    space: float | None = Field(
        default=None,
        description="Length of the space after the dash in points. Defaults to `length` if not provided.",
    )


class LineStyle(BaseModel):
    """Defines the style of a line, currently supporting dash patterns. (Primarily for table cell borders in some contexts)."""

    dash: Dash | None = Field(default=None, description="Dash pattern for the line.")
