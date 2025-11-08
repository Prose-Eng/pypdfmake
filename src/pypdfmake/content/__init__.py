"""Content model exports for pypdfmake."""

from pypdfmake.content.base import ContentBase, ContentLink
from pypdfmake.content.text import ContentText
from pypdfmake.content.layout import ContentColumns, ContentStack
from pypdfmake.content.lists import (
    OrderedListType,
    UnorderedListType,
    OrderedListElementProperties,
    UnorderedListElementProperties,
    OrderedListElement,
    UnorderedListElement,
    ContentOrderedList,
    ContentUnorderedList,
)
from pypdfmake.content.canvas import (
    CanvasLineCap,
    CanvasLineJoin,
    CanvasElementProperties,
    CanvasRect,
    CanvasLine,
    CanvasPolyline,
    CanvasEllipse,
    CanvasElement,
    ContentCanvas,
)
from pypdfmake.content.image import (
    ImageAlignment,
    ImageVerticalAlignment,
    ImageCover,
    ContentImage,
    ContentSvg,
)
from pypdfmake.content.table import (
    CustomTableLayout,
    PredefinedTableLayout,
    TableLayout,
    TableCell,
    Table,
    ContentTable,
)
from pypdfmake.content.references import (
    ContentAnchor,
    ContentPageReference,
    ContentTextReference,
    TableOfContent,
    ContentToc,
    ContentTocItem,
)
from pypdfmake.content.qr import ContentQr

__all__ = [
    # Base
    "ContentBase",
    "ContentLink",
    # Text
    "ContentText",
    # Layout
    "ContentColumns",
    "ContentStack",
    # Lists
    "OrderedListType",
    "UnorderedListType",
    "OrderedListElementProperties",
    "UnorderedListElementProperties",
    "OrderedListElement",
    "UnorderedListElement",
    "ContentOrderedList",
    "ContentUnorderedList",
    # Canvas
    "CanvasLineCap",
    "CanvasLineJoin",
    "CanvasElementProperties",
    "CanvasRect",
    "CanvasLine",
    "CanvasPolyline",
    "CanvasEllipse",
    "CanvasElement",
    "ContentCanvas",
    # Image
    "ImageAlignment",
    "ImageVerticalAlignment",
    "ImageCover",
    "ContentImage",
    "ContentSvg",
    # Table
    "CustomTableLayout",
    "PredefinedTableLayout",
    "TableLayout",
    "TableCell",
    "Table",
    "ContentTable",
    # References
    "ContentAnchor",
    "ContentPageReference",
    "ContentTextReference",
    "TableOfContent",
    "ContentToc",
    "ContentTocItem",
    # QR
    "ContentQr",
]

# Rebuild all content models to resolve forward references (AnyContent)
# This must happen after all content types are defined
ContentText.model_rebuild()  # Can reference itself recursively
ContentColumns.model_rebuild()
ContentStack.model_rebuild()
ContentOrderedList.model_rebuild()
ContentUnorderedList.model_rebuild()
OrderedListElement.model_rebuild()
UnorderedListElement.model_rebuild()
Table.model_rebuild()
ContentTable.model_rebuild()
ContentAnchor.model_rebuild()
ContentPageReference.model_rebuild()
ContentTextReference.model_rebuild()
TableOfContent.model_rebuild()
ContentToc.model_rebuild()
ContentTocItem.model_rebuild()
