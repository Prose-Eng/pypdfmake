"""Style-related type definitions for pypdfmake."""

from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field
from pypdfmake.types.base import Size, Margins, Decoration, DecorationStyle, Alignment
from pypdfmake.types.page import PageBreak, PageOrientation


class Style(BaseModel):
    """Defines a style that can be applied to content elements, affecting their appearance and layout."""

    font: str | None = Field(
        default=None,
        description="Name of the font family (must be defined in `fonts` dictionary).",
    )
    fontSize: float | None = Field(default=None, description="Font size in points.")
    fontFeatures: list[str] | None = Field(
        default=None, description="OpenType font features (e.g., ['smcp', 'liga=0'])."
    )
    bold: bool | None = Field(default=None, description="Apply bold style.")
    italics: bool | None = Field(default=None, description="Apply italic style.")
    characterSpacing: float | None = Field(
        default=None, description="Space between characters in points."
    )
    lineHeight: float | None = Field(
        default=None,
        description="Line height as a multiplier of font size (e.g., 1.5) or absolute points.",
    )
    color: str | None = Field(
        default=None, description="Text color (e.g., 'blue', '#00ff00')."
    )
    background: str | None = Field(
        default=None, description="Background color of the text block."
    )
    markerColor: str | None = Field(
        default=None, description="Color of list markers (bullets/numbers)."
    )
    decoration: Decoration | None = Field(
        default=None, description="Text decoration ('underline', 'strike', 'overline')."
    )
    decorationStyle: DecorationStyle | None = Field(
        default=None,
        description="Style of the decoration ('dashed', 'dotted', 'double', 'wavy').",
    )
    decorationColor: str | None = Field(
        default=None, description="Color of the decoration."
    )
    alignment: Alignment | None = Field(
        default=None,
        description="Text alignment ('left', 'right', 'center', 'justify').",
    )
    margin: Margins | None = Field(
        default=None, description="Margins around the element."
    )
    width: Size | None = Field(default=None, description="Width of the element.")
    height: Size | None = Field(default=None, description="Height of the element.")
    opacity: float | None = Field(
        default=None, description="Opacity of the element (0.0 to 1.0)."
    )
    leadingIndent: float | None = Field(
        default=None, description="Indentation for the first line of a paragraph."
    )
    preserveLeadingSpaces: bool | None = Field(
        default=None, description="If true, preserve leading spaces in text."
    )
    preserveTrailingSpaces: bool | None = Field(
        default=None, description="If true, preserve trailing spaces in text."
    )
    noWrap: bool | None = Field(
        default=None, description="If true, prevent text from wrapping."
    )
    pageBreak: PageBreak | None = Field(
        default=None, description="Page break behavior before or after the element."
    )
    pageOrientation: PageOrientation | None = Field(
        default=None,
        description="Specific page orientation for the page this element starts on.",
    )
    headlineLevel: int | None = Field(
        default=None, description="Headline level for accessibility and TOC generation."
    )
    # Table cell specific properties
    fillColor: str | None = Field(
        default=None, description="Background color for table cells or canvas shapes."
    )
    rowSpan: int | None = Field(
        default=None, description="Number of rows this table cell should span."
    )
    colSpan: int | None = Field(
        default=None, description="Number of columns this table cell should span."
    )
    border: list[bool] | None = Field(
        default=None,
        description="Border for table cells: `[left, top, right, bottom]`. True for default line, False for no line.",
    )
    borderColor: str | list[str] | None = Field(
        default=None,
        description="Border color for table cells. Single color or `[left, top, right, bottom]`.",
    )
    verticalAlignment: Literal["top", "center", "bottom"] | None = Field(
        default=None, description="Vertical alignment within a table cell."
    )
    # Style inheritance
    style: str | list[str] | None = Field(
        default=None,
        description="Name of a style or list of style names to inherit from.",
    )
    model_config = {
        "extra": "allow"
    }  # Allow other properties for pdfmake compatibility


StyleReference = str | Style | list[str | Style]
"""A reference to a style: can be a style name (string), a Style object, or a list of these for cascading styles."""

StyleDictionary = dict[str, Style]
"""A dictionary mapping style names (e.g., 'headerStyle') to Style objects."""
