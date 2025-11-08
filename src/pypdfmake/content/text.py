"""Text content classes for pypdfmake."""

from __future__ import annotations
from pydantic import Field
from pypdfmake.content.base import ContentBase, ContentLink


class ContentText(ContentBase, ContentLink):
    """
    Represents a text block. Can be a simple string or a list of mixed string and styled text objects
    for complex inline styling.
    """

    text: str | int | list[str | int | ContentText] = Field(
        description="The text content. Can be a string, number, or a list of strings, numbers, or other `ContentText` objects for complex inline styling and mixed formatting."
    )

