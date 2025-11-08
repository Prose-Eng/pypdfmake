"""Document definition classes for pypdfmake."""

from __future__ import annotations
from typing import Union
from pydantic import BaseModel, Field

from pypdfmake.content import (
    ContentCanvas,
    ContentColumns,
    ContentImage,
    ContentOrderedList,
    ContentPageReference,
    ContentQr,
    ContentStack,
    ContentSvg,
    ContentTable,
    ContentText,
    ContentTextReference,
    ContentToc,
    ContentUnorderedList,
)
from pypdfmake.types.base import Margins
from pypdfmake.types.page import PageSize, PageOrientation
from pypdfmake.types.style import Style, StyleDictionary
from pypdfmake.types.callable import DynamicContentCallable, DynamicBackgroundCallable
from pypdfmake.document.info import TDocumentInformation, PDFVersion, PDFSubset, Watermark
from pypdfmake.document.fonts import TFontDictionary
from pypdfmake.document.patterns import PatternDictionary, ImageDictionary

# Import AnyContent and ContentTypes from central location
from pypdfmake.types.content import AnyContent, ContentTypes


class TDocumentDefinitions(BaseModel):
    """The root object for a pdfmake document definition, containing all content, styles, metadata, and document-level settings."""

    content: Union[AnyContent, list[AnyContent | str]] = Field(
        description="The main content of the document. Can be a single content element or an array of elements."
    )
    styles: StyleDictionary | None = Field(
        default=None,
        description="A dictionary of named styles that can be referenced by content elements.",
    )
    defaultStyle: Style | None = Field(
        default=None,
        description="The default style applied to all text elements unless overridden.",
    )
    pageSize: PageSize | None = Field(
        default=None,
        description="Page size of the document (e.g., 'A4', or a custom `{width, height}`). Default: 'A4'.",
    )
    pageOrientation: PageOrientation | None = Field(
        default=None,
        description="Page orientation ('portrait' or 'landscape'). Default: 'portrait'.",
    )
    pageMargins: Margins | None = Field(
        default=None,
        description="Margins for pages `[left, top, right, bottom]` or a single value. Default: `[40, 60, 40, 60]` (approx).",
    )
    header: Union[AnyContent, DynamicContentCallable, None] = Field(
        default=None,
        description="Content for the page header. Can be static content or a function `(currentPage, pageCount, pageSize) => content`.",
    )
    footer: Union[AnyContent, DynamicContentCallable, None] = Field(
        default=None,
        description="Content for the page footer. Can be static content or a function `(currentPage, pageCount, pageSize) => content`.",
    )
    background: Union[AnyContent, DynamicBackgroundCallable, None] = Field(
        default=None,
        description="Background content for all pages. Can be static or a function `(currentPage, pageSize) => content`.",
    )
    images: ImageDictionary | None = Field(
        default=None,
        description="A dictionary of images, where keys are names used in `ContentImage.image` and values are image data (base64 or URL).",
    )
    fonts: TFontDictionary | None = Field(
        default=None,
        description="A dictionary defining custom fonts and their font family types.",
    )
    patterns: PatternDictionary | None = Field(
        default=None,
        description="A dictionary of named patterns that can be used for backgrounds or fills.",
    )
    watermark: str | Watermark | None = Field(
        default=None,
        description="A watermark to be displayed on pages. Can be a simple string or a `Watermark` object for more options.",
    )
    info: TDocumentInformation | None = Field(
        default=None, description="Metadata for the PDF document (title, author, etc.)."
    )
    compress: bool = Field(
        default=True, description="Whether to compress the PDF content. Default: true."
    )
    userPassword: str | None = Field(
        default=None, description="Password required to open the PDF (user password)."
    )
    ownerPassword: str | None = Field(
        default=None,
        description="Password required to change permissions or the user password (owner password).",
    )
    permissions: dict[str, bool] | None = Field(
        default=None,
        description="Permissions for the PDF (e.g., `{ printing: 'highResolution', modifying: false }`).",
    )
    defaultFont: str | None = Field(
        default=None,
        description="Sets the default font for the document if not specified in defaultStyle. Overrides VFS fonts like Roboto.",
    )
    version: PDFVersion | None = Field(
        default=None, description="PDF version for the output document."
    )
    subset: PDFSubset | None = Field(
        default=None, description="Specifies a PDF subset standard (e.g., PDF/A)."
    )
    author: str | None = Field(default=None, description="Shortcut for `info.author`.")
    creator: str = Field(
        default="pypdfmake",
        description="Shortcut for `info.creator`. Defaults to 'pypdfmake'.",
    )
    model_config = {"extra": "allow"}
