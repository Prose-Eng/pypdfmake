"""Font-related classes for pypdfmake."""

from __future__ import annotations
from pydantic import BaseModel, Field


class TFontFamilyTypes(BaseModel):
    """Defines font files for different styles (normal, bold, italics, bolditalics) within a font family."""

    normal: str | None = Field(
        default=None,
        description="Path or reference to the normal (roman) font file/stream.",
    )
    bold: str | None = Field(
        default=None, description="Path or reference to the bold font file/stream."
    )
    italics: str | None = Field(
        default=None, description="Path or reference to the italics font file/stream."
    )
    bolditalics: str | None = Field(
        default=None,
        description="Path or reference to the bold-italics font file/stream.",
    )


TFontDictionary = dict[str, TFontFamilyTypes]
"""A dictionary mapping font family names (e.g., 'Roboto') to their TFontFamilyTypes definitions."""
