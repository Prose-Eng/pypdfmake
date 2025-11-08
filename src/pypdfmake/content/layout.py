"""Layout content classes for pypdfmake."""

from __future__ import annotations
from pydantic import Field

from pypdfmake.types.content import AnyContent
from pypdfmake.content.base import ContentBase


class ContentColumns(ContentBase):
    """Defines a layout with multiple columns. Content flows from one column to the next."""

    columns: list[AnyContent] = Field(
        description="A list of content elements, each representing a column. Content can be simple text or complex structures."
    )
    columnGap: float | None = Field(
        default=None, description="The space between columns in points."
    )


class ContentStack(ContentBase):
    """Stacks content elements vertically. Each element in the stack is placed below the previous one."""

    stack: list[AnyContent] = Field(
        description="A list of content elements to be stacked vertically."
    )
