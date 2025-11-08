"""Document information and metadata classes for pypdfmake."""

from __future__ import annotations
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field

PDFSubset = Literal["PDF/A-1B", "PDF/A-2B", "PDF/A-3B", "PDF/X-3"]
"""Specifies a PDF subset standard for archival or print purposes (e.g., 'PDF/A-1B')."""

PDFVersion = Literal["1.3", "1.4", "1.5", "1.6", "1.7", "1.7ext3"]
"""Specifies the PDF version for the output document (e.g., '1.7')."""


class TDocumentInformation(BaseModel):
    """Metadata for the PDF document (e.g., title, author, subject)."""

    title: str | None = Field(default=None, description="The title of the document.")
    author: str | None = Field(default=None, description="The author of the document.")
    subject: str | None = Field(
        default=None, description="The subject of the document."
    )
    keywords: str | None = Field(
        default=None,
        description="Keywords associated with the document, comma-separated.",
    )
    producer: str | None = Field(
        default=None,
        description="The producer of the PDF. pdfmake sets its own default.",
    )
    creator: str | None = Field(
        default=None, description="The creator of the PDF. pypdfmake sets a default."
    )
    creationDate: datetime = Field(
        default_factory=datetime.now,
        description="The creation date of the document. Defaults to current time.",
    )
    modDate: datetime = Field(
        default_factory=datetime.now,
        description="The modification date of the document. Defaults to current time.",
    )
    trapped: str | None = Field(
        default=None,
        description="Trapping information for the document (e.g., 'True', 'False', 'Unknown').",
    )


class Watermark(BaseModel):
    """Defines a watermark (text or image) to be displayed on pages, typically in the background."""

    text: str = Field(description="The text content of the watermark.")
    font: str | None = Field(
        default=None,
        description="Font for the watermark text. Must be defined in `fonts` dictionary.",
    )
    fontSize: float | None = Field(
        default=None, description="Font size for the watermark text in points."
    )
    color: str | None = Field(
        default=None, description="Color of the watermark text. Default: 'black'."
    )
    opacity: float | None = Field(
        default=None, description="Opacity of the watermark (0.0 to 1.0). Default: 0.5."
    )
    bold: bool | None = Field(
        default=None, description="Whether the watermark text is bold."
    )
    italics: bool | None = Field(
        default=None, description="Whether the watermark text is italic."
    )
    angle: float | None = Field(
        default=None,
        description="Rotation angle of the watermark text in degrees. Default: 0.",
    )
