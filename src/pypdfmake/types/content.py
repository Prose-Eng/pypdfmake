"""Content type definitions for pypdfmake."""

from __future__ import annotations
from typing import Union

# Define basic content types using forward references to avoid circular imports
ContentTypes = Union[
    "ContentText",
    "ContentColumns", 
    "ContentStack",
    "ContentOrderedList",
    "ContentUnorderedList", 
    "ContentCanvas",
    "ContentImage",
    "ContentSvg",
    "ContentTable",
    "ContentPageReference",
    "ContentTextReference",
    "ContentToc",
    "ContentQr",
    str,
]

# Define AnyContent to include both basic types and lists of those types
AnyContent = Union[ContentTypes, list[ContentTypes]]
"""
A union of all possible content element types that can be part of the document body
or complex structures like columns, stacks, lists, etc.
Forward references (strings) are used here for each Pydantic model and should be
resolved by appropriate `Model.model_rebuild()` calls at the end of the module
for all involved models.
"""