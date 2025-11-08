"""Pattern and image definition classes for pypdfmake."""

from __future__ import annotations
from pydantic import BaseModel, Field

from pypdfmake.content.canvas import CanvasElement


class Pattern(BaseModel):
    """Defines a repeating pattern for backgrounds or fills, using vector graphics (canvas) or SVG."""

    boundingBox: list[float] = Field(
        description="The bounding box `[x1, y1, x2, y2]` of one instance of the pattern cell in points."
    )
    xStep: float = Field(
        description="Horizontal step size in points for repeating the pattern."
    )
    yStep: float = Field(
        description="Vertical step size in points for repeating the pattern."
    )
    canvas: list[CanvasElement] | None = Field(
        default=None, description="Canvas elements to draw one instance of the pattern."
    )
    svg: str | None = Field(
        default=None,
        description="SVG content string to use as one instance of the pattern.",
    )


PatternDictionary = dict[str, Pattern]
"""A dictionary mapping pattern names to Pattern objects, for use in `background` or `fillColor` properties."""


class ImageDefinition(BaseModel):
    """Defines an image by its URL, typically for remote images to be fetched by pdfmake if not provided as base64."""

    url: str = Field(
        description="URL of the image (e.g., 'https://example.com/image.png')."
    )


ImageDictionary = dict[str, str | ImageDefinition]
"""
A dictionary mapping image names (keys) to image data.
Values can be:
- A base64 encoded image string (e.g., 'data:image/jpeg;base64,...').
- A URL string (if pdfmake is configured to fetch remote images).
- An `ImageDefinition` object (primarily for specifying URLs, potentially with headers).
"""
