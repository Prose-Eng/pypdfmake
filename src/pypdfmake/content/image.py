"""Image content classes for pypdfmake."""

from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field
from pypdfmake.content.base import ContentBase, ContentLink
from pypdfmake.types.base import Size, Position
from pypdfmake.types.page import PageBreak

ImageAlignment = Literal["left", "right", "center"]
"""Horizontal alignment for images within their bounding box if `cover` is used or if the image has fixed dimensions smaller than available space."""

ImageVerticalAlignment = Literal["top", "bottom", "center"]
"""Vertical alignment for images, similar to `ImageAlignment` but for the vertical axis."""


class ImageCover(BaseModel):
    """
    Defines how an image should cover its container, similar to CSS `background-size: cover`.
    The image is scaled to maintain its aspect ratio while filling the element's entire content box.
    If the image's aspect ratio does not match the aspect ratio of its box, then the image will be clipped to fit.
    """

    width: float | None = Field(
        default=None,
        description="Target width for the cover area. Image will be scaled to cover this width.",
    )
    height: float | None = Field(
        default=None,
        description="Target height for the cover area. Image will be scaled to cover this height.",
    )
    align: ImageAlignment | None = Field(
        default=None,
        description="Horizontal alignment of the image within the covered area if aspect ratios differ.",
    )
    valign: ImageVerticalAlignment | None = Field(
        default=None,
        description="Vertical alignment of the image within the covered area if aspect ratios differ.",
    )


class ContentImage(ContentBase, ContentLink):
    """Represents an image to be embedded in the document."""

    image: str = Field(
        description="The key of the image in the `images` dictionary (defined at the document root) or a base64 encoded image string (e.g., 'data:image/jpeg;base64,...')."
    )
    width: Size | None = Field(
        default=None,
        description="Width of the image in points. If undefined, uses natural image width.",
    )
    height: Size | None = Field(
        default=None,
        description="Height of the image in points. If undefined, uses natural image height.",
    )
    fit: tuple[float, float] | None = Field(
        default=None,
        description="Tuple `[maxWidth, maxHeight]` to scale the image to fit within these dimensions while maintaining aspect ratio.",
    )
    cover: ImageCover | None = Field(
        default=None,
        description="Cover options for the image, allowing it to fill a specified area, potentially being cropped.",
    )
    pageBreak: PageBreak | None = Field(
        default=None, description="Page break behavior before or after the image."
    )
    absolutePosition: Position | None = Field(
        default=None,
        description="Position the image absolutely on the page at `(x, y)` coordinates.",
    )
    relativePosition: Position | None = Field(
        default=None,
        description="Position the image relative to its normal flow position by `(x, y)` offset.",
    )
    opacity: float | None = Field(
        default=None, description="Opacity of the image (0.0 to 1.0)."
    )


class ContentSvg(ContentBase, ContentLink):
    """Represents an SVG image to be embedded in the document."""

    svg: str = Field(
        description="The SVG content as a string (e.g., '<svg>...</svg>')."
    )
    width: Size | None = Field(
        default=None,
        description="Width to render the SVG in points. If undefined, may use SVG's native width.",
    )
    height: Size | None = Field(
        default=None,
        description="Height to render the SVG in points. If undefined, may use SVG's native height.",
    )
    fit: tuple[float, float] | None = Field(
        default=None,
        description="Tuple `[maxWidth, maxHeight]` to scale the SVG to fit within these dimensions while maintaining aspect ratio.",
    )
