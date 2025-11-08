"""Reference content classes for pypdfmake."""

from __future__ import annotations
from pydantic import BaseModel, Field

from pypdfmake.types.content import AnyContent
from pypdfmake.content.base import ContentBase
from pypdfmake.content.text import ContentText
from pypdfmake.types.base import Margins
from pypdfmake.types.style import StyleReference


class ContentAnchor(ContentBase):
    """
    Represents a text element that can also serve as a named destination (anchor) if an `id` is provided.
    Primarily, link destinations are created by assigning an `id` to any content element.
    """

    text: str | int | list[str | int | ContentText] = Field(
        description="The visible text content of this element. If an `id` is set (from `ContentBase`), this element can be a link target."
    )


class ContentPageReference(ContentBase):
    """Displays the page number where a referenced element (identified by its `id`) appears."""

    pageReference: str = Field(
        description="The `id` of the content element whose page number is to be displayed."
    )
    text: str | int | ContentText | None = Field(
        default=None,
        description="Optional text to display alongside the page number. Can be a simple string or a styled `ContentText` object. The page number is typically inserted where a special placeholder might be used or appended/prepended.",
    )


class ContentTextReference(ContentBase):
    """Displays the text content of another element (identified by its `id`)."""

    textReference: str = Field(
        description="The `id` of the content element whose text content is to be displayed."
    )
    text: str | int | ContentText | None = Field(
        default=None,
        description="Optional text to display alongside the referenced text. Can be a simple string or a styled `ContentText` object.",
    )


class TableOfContent(BaseModel):  # Corresponds to 'toc' property in ContentToc
    """Defines the properties for a Table of Contents (TOC)."""

    title: AnyContent | None = Field(
        default=None,
        description="Optional title for the Table of Contents (e.g., a `ContentText` object).",
    )
    textMargin: Margins | None = Field(
        default=None, description="Margins for individual TOC entries."
    )
    textStyle: StyleReference | None = Field(
        default=None, description="Style to be applied to TOC entries (text part)."
    )
    id: str | None = Field(
        default=None,
        description="Optional `id` for the Table of Contents block itself, making it a linkable target.",
    )


class ContentToc(ContentBase):
    """Generates a Table of Contents based on elements marked with `tocItem` or `headlineLevel`."""

    toc: TableOfContent = Field(
        description="The `TableOfContent` definition object specifying the appearance and behavior of the TOC."
    )


class ContentTocItem(ContentBase):
    """
    Represents an explicit item to be included in the Table of Contents.
    More commonly, items are added to the TOC by setting the `tocItem` property on other content elements.
    """

    text: str | int | list[str | int | ContentText] = Field(
        description="The text of the TOC item as it should appear in the TOC."
    )
