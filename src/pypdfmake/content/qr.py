"""QR code content classes for pypdfmake."""

from __future__ import annotations
from typing import Literal
from pydantic import Field
from pypdfmake.content.base import ContentBase


class ContentQr(ContentBase):
    """Generates a QR code image."""

    qr: str = Field(description="The text content to encode in the QR code.")
    foreground: str | None = Field(
        default=None,
        description="Color of the QR code modules (dots). Default: 'black'.",
    )
    background: str | None = Field(
        default=None, description="Color of the QR code background. Default: 'white'."
    )
    version: int | None = Field(
        default=None,
        description="QR code version (1-40). Determines data capacity. Auto-selected if None.",
    )
    eccLevel: Literal["L", "M", "Q", "H"] | None = Field(
        default=None,
        description="Error correction capability level (Low, Medium, Quartile, High). Default: 'M'.",
    )
    fit: float | None = Field(
        default=None,
        description="Size (width and height) of the QR code in points. Default: 100.",
    )
    padding: float | None = Field(
        default=None,
        description="Padding around the QR code in modules (QR code 'pixels'). Default: 0.",
    )
    mode: Literal["numeric", "alphanumeric", "byte", "kanji"] | None = Field(
        default=None, description="Encoding mode. Auto-selected if None."
    )
    maskPattern: Literal[0, 1, 2, 3, 4, 5, 6, 7] | None = Field(
        default=None,
        description="Mask pattern for the QR code. Auto-selected if None (0-7).",
    )
