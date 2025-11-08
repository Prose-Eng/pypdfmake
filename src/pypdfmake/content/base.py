"""Base content classes for pypdfmake."""

from __future__ import annotations
from pydantic import BaseModel, Field
from pypdfmake.types.style import Style, StyleReference
from pypdfmake.types.base import Margins


class ContentBase(Style):
    """Base class for content elements, providing common styling capabilities and Table of Contents (TOC) properties."""

    id: str | None = Field(
        default=None,
        description="An optional identifier for the content element. Used for page references, text references, or as a link target.",
    )
    tocItem: bool | StyleReference | None = Field(
        default=None,
        description="If true or a StyleReference, this item will be included in the Table of Contents. The StyleReference can style the TOC entry.",
    )
    tocStyle: StyleReference | None = Field(
        default=None,
        description="Style to be applied specifically to this item's entry in the Table of Contents.",
    )
    tocMargin: Margins | None = Field(
        default=None,
        description="Margins for this item's entry in the Table of Contents.",
    )


class ContentLink(BaseModel):
    """Properties for creating hyperlinks within content elements like text or images."""

    link: str | None = Field(
        default=None,
        description="An external URL to link to (e.g., 'https://example.com').",
    )
    linkToPage: int | None = Field(
        default=None,
        description="A 1-based page number to link to within the current document.",
    )
    linkToDestination: str | None = Field(
        default=None,
        description="The `id` of a content element to link to within the current document.",
    )
