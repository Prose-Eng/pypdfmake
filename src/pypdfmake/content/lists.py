"""List content classes for pypdfmake."""

from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field

from pypdfmake.types.content import AnyContent
from pypdfmake.content.base import ContentBase
from pypdfmake.content.text import ContentText

OrderedListType = Literal[
    "none",  # No marker
    "decimal",  # 1, 2, 3,...
    "lower-alpha",  # a, b, c,...
    "upper-alpha",  # A, B, C,...
    "lower-roman",  # i, ii, iii,...
    "upper-roman",  # I, II, III,...
]
"""Marker types for ordered lists (e.g., '1.', 'a.', 'A.', 'i.', 'I.'). Defaults to 'decimal'."""

UnorderedListType = Literal[
    "disc",  # Default, filled circle
    "circle",  # Hollow circle
    "square",  # Filled square
    "none",  # No marker
]
"""Marker types for unordered lists (bullet styles, e.g., 'disc', 'circle', 'square'). Defaults to 'disc' (bullet)."""


class OrderedListElementProperties(BaseModel):
    """Properties that can be applied to items in an ordered list."""

    counter: int | None = Field(
        default=None,
        description="Overrides the counter for this list item. Does not influence counters for other list items.",
    )
    type: OrderedListType | None = Field(
        default=None,
        description="Overrides the list marker type for this list item.",
    )


class UnorderedListElementProperties(BaseModel):
    """Properties that can be applied to items in an unordered list."""

    type: UnorderedListType | None = Field(
        default=None,
        description="Overrides the list marker type for this list item.",
    )


class OrderedListElement(ContentBase, OrderedListElementProperties):
    """
    Represents an item in an ordered list, combining content and list-specific properties.
    """

    text: str | int | list[str | int | ContentText] = Field(
        description="The text content of the list item. Can be a string, number, or a list of mixed content."
    )


class UnorderedListElement(ContentBase, UnorderedListElementProperties):
    """
    Represents an item in an unordered list, combining content and list-specific properties.
    """

    text: str | int | list[str | int | ContentText] = Field(
        description="The text content of the list item. Can be a string, number, or a list of mixed content."
    )


class ContentOrderedList(ContentBase):
    """Represents an ordered list (e.g., numbered or lettered)."""

    ol: list[AnyContent | str | OrderedListElement] = Field(
        description="A list of content elements, each representing a list item."
    )
    type: OrderedListType | None = Field(
        default=None,
        description="The type of marker for the list items (e.g., 'lower-alpha', 'upper-roman'). Defaults to decimal numbers.",
    )
    reversed: bool | None = Field(
        default=None,
        description="If true, the list numbering will be in reverse order.",
    )
    start: int | None = Field(
        default=None, description="The starting number for the list (e.g., start at 5)."
    )
    separator: str | list[str] | None = Field(
        default=None,
        description="Custom separator for list items. Can be a single string (e.g., ')') or a [before, after] list (e.g., ['(', ')']).",
    )


class ContentUnorderedList(ContentBase):
    """Represents an unordered list (e.g., bulleted)."""

    ul: list[AnyContent | str | UnorderedListElement] = Field(
        description="A list of content elements, each representing a list item."
    )
    type: UnorderedListType | None = Field(
        default=None,
        description="The type of marker for the list items (e.g., 'square', 'circle'). Defaults to 'bullet'.",
    )
