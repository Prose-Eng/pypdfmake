"""Table content classes for pypdfmake."""

from __future__ import annotations
from typing import Literal, Any, Union
from pydantic import BaseModel, Field

from pypdfmake.types.content import AnyContent
from pypdfmake.content.base import ContentBase
from pypdfmake.types.base import Size
from pypdfmake.types.callable import (
    DynamicRowSizeCallable,
    DynamicLayoutCallable,
    VerticalDynamicLayoutCallable,
    DynamicCellLayoutCallable,
)


class CustomTableLayout(BaseModel):
    """
    Defines a custom layout for tables, allowing dynamic control over line widths, colors, styles,
    cell padding, and fill colors.
    """

    hLineWidth: DynamicLayoutCallable | None = Field(
        default=None,
        description="Callable to determine horizontal line width. Receives `(i, node)`, returns line width. `i` is line index.",
    )
    vLineWidth: VerticalDynamicLayoutCallable | None = Field(
        default=None,
        description="Callable to determine vertical line width. Receives `(i, node)`, returns line width. `i` is line index.",
    )
    hLineColor: DynamicLayoutCallable | None = Field(
        default=None,
        description="Callable to determine horizontal line color. Receives `(i, node)`, returns color string.",
    )
    vLineColor: VerticalDynamicLayoutCallable | None = Field(
        default=None,
        description="Callable to determine vertical line color. Receives `(i, node)`, returns color string.",
    )
    hLineStyle: DynamicLayoutCallable | None = Field(
        default=None,
        description="Callable to determine horizontal line style (e.g., dash pattern). Receives `(i, node)`. ",
    )
    vLineStyle: VerticalDynamicLayoutCallable | None = Field(
        default=None,
        description="Callable to determine vertical line style. Receives `(i, node)`. ",
    )
    paddingLeft: DynamicLayoutCallable | None = Field(
        default=None,
        description="Callable to determine left padding of cells in a column. Receives `(i, node)`, `i` is column index.",
    )
    paddingRight: DynamicLayoutCallable | None = Field(
        default=None,
        description="Callable to determine right padding of cells in a column. Receives `(i, node)`, `i` is column index.",
    )
    paddingTop: DynamicCellLayoutCallable | None = Field(
        default=None,
        description="Callable to determine top padding of a cell. Receives `(i, node, j)`, `i` is row index, `j` is col index.",
    )
    paddingBottom: DynamicCellLayoutCallable | None = Field(
        default=None,
        description="Callable to determine bottom padding of a cell. Receives `(i, node, j)`, `i` is row index, `j` is col index.",
    )
    fillColor: DynamicCellLayoutCallable | None = Field(
        default=None,
        description="Callable to determine background fill color of a cell. Receives `(i, node, j)`, `i` is row index, `j` is col index.",
    )
    defaultBorder: bool | None = Field(
        default=None,
        description="If true, draws default borders for cells unless overridden by cell's `border` property. Default is true.",
    )


PredefinedTableLayout = Literal["noBorders", "headerLineOnly", "lightHorizontalLines"]
"""Standard predefined table layouts: 'noBorders', 'headerLineOnly', 'lightHorizontalLines'."""

TableLayout = str | PredefinedTableLayout | CustomTableLayout
"""
Represents a table layout.
Can be:
- A predefined layout name string (e.g., 'noBorders').
- A `CustomTableLayout` object for full control.
- A string referring to a custom layout defined in the `tableLayouts` dictionary at the document root (not directly modeled here, but a string value implies this).
"""

# Now define TableCell type alias, using the now-defined AnyContent
TableCell = Union[
    AnyContent, dict[str, Any]
]  # dict[str, Any] is a fallback, ideally cells are specific content types.
"""
Represents the content of a table cell.
Can be:
- Any `AnyContent` type (e.g., a string, `ContentText`, `ContentImage`).
- A dictionary, which pdfmake often interprets as a `ContentText`-like object if it has a `text` key, or other content types if structured accordingly.
  It's generally recommended to use explicit Pydantic models for cell content for better type safety.
"""


class Table(BaseModel):
    """Defines the structure and content of a table, including its body, column widths, row heights, and header behavior."""

    body: list[list[TableCell]] = Field(
        description="A 2D array representing the table rows and cells. Each cell is `TableCell` content."
    )
    widths: list[Size] | None = Field(
        default=None,
        description="List of column widths. Can be fixed numbers (points), '*', or 'auto'. If undefined, columns are equally sized.",
    )
    heights: float | list[float | Literal["auto"]] | DynamicRowSizeCallable | None = (
        Field(
            default=None,
            description="List of row heights (points or 'auto'), or a callable `(rowIndex) => height` for dynamic row heights.",
        )
    )
    headerRows: int | None = Field(
        default=None,
        description="Number of rows from the beginning of `body` to repeat as a header on subsequent pages if the table spans multiple pages.",
    )
    keepWithHeaderRows: int | None = Field(
        default=None,
        description="Number of body rows (after headerRows) to keep with the header rows when a page break occurs within the table.",
    )
    layout: TableLayout | None = Field(
        default=None,
        description="Overrides the layout defined in `ContentTable.layout` specifically for this table's internal structure. Not commonly used here, `ContentTable.layout` is primary.",
    )


class ContentTable(ContentBase):
    """Represents a table with rows, columns, and an optional layout."""

    table: Table = Field(
        description="The `Table` object containing the body (rows and cells), column widths, row heights, and header definitions."
    )
    layout: TableLayout | None = Field(
        default=None,
        description="The layout to apply to the table. Can be a predefined string (e.g., 'lightHorizontalLines'), a custom layout object, or a string key for a layout defined in `documentDefinition.tableLayouts`.",
    )
