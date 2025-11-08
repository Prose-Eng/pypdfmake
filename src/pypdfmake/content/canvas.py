"""Canvas content classes for pypdfmake."""

from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field
from pypdfmake.content.base import ContentBase
from pypdfmake.types.base import Point, Dash

CanvasLineCap = Literal["butt", "round", "square"]
"""Defines the style for the end caps of a line in a canvas: 'butt', 'round', or 'square'."""

CanvasLineJoin = Literal["miter", "round", "bevel"]
"""Defines the style for the joins between two lines in a canvas: 'miter', 'round', or 'bevel'."""


class CanvasElementProperties(BaseModel):
    """Base properties for canvas elements, including line, fill, and general styling."""

    lineColor: str | None = Field(
        default=None,
        description="Color of the line for vector shapes (e.g., 'red', '#0000FF'). Default is 'black' if a line is drawn.",
    )
    lineWidth: float = Field(default=1, description="Width of the line in points.")
    lineCap: CanvasLineCap | None = Field(
        default=None, description="Style of line end caps."
    )
    lineJoin: CanvasLineJoin | None = Field(
        default=None,
        description="Style of line joins when multiple line segments meet.",
    )
    dash: Dash | None = Field(
        default=None,
        description="Dash pattern for lines (e.g., `{ length: 4, space: 2 }`).",
    )
    miterLimit: float | None = Field(
        default=None,
        description="Miter limit for line joins when `lineJoin` is 'miter'.",
    )
    fillColor: str | None = Field(
        default=None, description="Color to fill the shape (e.g., 'yellow', '#FFFF00')."
    )
    fillOpacity: float | None = Field(
        default=None, description="Opacity of the fill (0.0 to 1.0)."
    )
    color: str | None = Field(
        default=None,
        description="General color property. Can act as a shorthand for `lineColor` or `fillColor` depending on the element, or for text color if the canvas element is text (not standard in pdfmake vector canvas).",
    )
    opacity: float | None = Field(
        default=None,
        description="General opacity for the entire canvas element (0.0 to 1.0).",
    )


class CanvasRect(CanvasElementProperties):
    """A rectangle canvas element."""

    type: Literal["rect"] = Field(
        default="rect", description="Type of canvas element, must be 'rect'."
    )
    x: float = Field(
        description="X-coordinate of the top-left corner of the rectangle."
    )
    y: float = Field(
        description="Y-coordinate of the top-left corner of the rectangle."
    )
    w: float = Field(description="Width of the rectangle.")
    h: float = Field(description="Height of the rectangle.")
    r: float | None = Field(
        default=None,
        description="Radius for rounded corners. If 0 or undefined, corners are square.",
    )


class CanvasLine(CanvasElementProperties):
    """A line canvas element, connecting two points."""

    type: Literal["line"] = Field(
        default="line", description="Type of canvas element, must be 'line'."
    )
    x1: float = Field(description="X-coordinate of the starting point of the line.")
    y1: float = Field(description="Y-coordinate of the starting point of the line.")
    x2: float = Field(description="X-coordinate of the ending point of the line.")
    y2: float = Field(description="Y-coordinate of the ending point of the line.")


class CanvasPolyline(CanvasElementProperties):
    """A polyline (series of connected lines) or polygon canvas element."""

    type: Literal["polyline"] = Field(
        default="polyline", description="Type of canvas element, must be 'polyline'."
    )
    points: list[Point] = Field(
        description="List of points `[(x, y), ...]` defining the vertices of the polyline."
    )
    closePath: bool | None = Field(
        default=None,
        description="If true, connects the last point to the first, effectively creating a polygon that can be filled.",
    )


class CanvasEllipse(CanvasElementProperties):
    """An ellipse or circle canvas element."""

    type: Literal["ellipse"] = Field(
        default="ellipse", description="Type of canvas element, must be 'ellipse'."
    )
    x: float = Field(description="X-coordinate of the center of the ellipse.")
    y: float = Field(description="Y-coordinate of the center of the ellipse.")
    r1: float = Field(description="Horizontal radius of the ellipse.")
    r2: float | None = Field(
        default=None,
        description="Vertical radius of the ellipse. If not provided, defaults to `r1` (creating a circle).",
    )


CanvasElement = CanvasRect | CanvasPolyline | CanvasLine | CanvasEllipse
"""Union type for all supported canvas vector elements."""


class ContentCanvas(ContentBase):
    """Allows drawing vector graphics using a canvas-like API within the document."""

    canvas: list[CanvasElement] = Field(
        description="A list of canvas elements (rectangles, lines, polylines, ellipses) to draw."
    )
