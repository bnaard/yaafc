from typing import Any

import polars as pl
import reflex as rx
from reflex.vars import ArrayVar


class TableState(rx.State):
    # Store the DataFrame as a class variable (not a field)
    _df = pl.DataFrame({
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"],
        "Age": [25, 30, 35, 28, 22, 40, 31, 29, 27, 33],
        "City": ["NY", "LA", "Chicago", "Boston", "Miami", "Dallas", "Seattle", "Denver", "Austin", "SF"],
    })

    page: int = 0
    page_size: int = 5

    @rx.var
    def total_pages(self) -> int:
        return (self._df.height + self.page_size - 1) // self.page_size

    @rx.var
    def columns(self) -> list[str]:
        return self._df.columns

    @rx.var
    def page_rows(self) -> list[tuple[Any, ...]]:
        start = self.page * self.page_size
        end = start + self.page_size
        return self._df.rows()[start:end]

    def next_page(self):
        if self.page < self.total_pages - 1:
            self.page += 1

    def prev_page(self):
        if self.page > 0:
            self.page -= 1


def table_header_cell(*children, **props) -> rx.Component:
    """Creates a table header cell with the given label."""
    return rx.table.column_header_cell(
        *children,
        border_right="solid",
        border_right_color=rx.color("accent", 4),
        border_right_width="1px",
        border_bottom="solid",
        border_bottom_color=rx.color("accent", 4),
        border_bottom_width="1px",
        background_color=rx.color("accent", 3),
        style={"position": "sticky", "top": "0"},
        **props,
    )


def table_header(columns: ArrayVar[list[str]]) -> rx.Component:
    """Creates a table header with the given column names."""
    return (rx.table.header(rx.table.row(rx.foreach(columns, lambda col: table_header_cell(col)))),)


def table_row_cell(*children, **props) -> rx.Component:
    """Creates a table row cell with the given data."""
    return rx.table.cell(
        *children,
        border_bottom="solid",
        border_bottom_color=rx.color("accent", 4),
        border_bottom_width="1px",
        background_color=rx.color("accent", 2),
        **props,
    )


def table_row(row: ArrayVar[tuple[Any, ...]]) -> rx.Component:
    """Creates a table row with the given data."""
    return rx.table.row(
        rx.foreach(row, lambda cell: table_row_cell(cell)),
    )


def table():
    columns = TableState.columns
    rows = TableState.page_rows

    return rx.box(
        rx.box(
            rx.table.root(
                table_header(columns),
                rx.table.body(
                    rx.foreach(
                        rows,
                        table_row,
                    ),
                ),
                width="100%",
                style={"minWidth": "600px"},  # Ensures table doesn't shrink too much
            ),
            overflow_x="auto",
            width="100%",
        ),
        rx.hstack(
            rx.button("Previous", on_click=TableState.prev_page, is_disabled=TableState.page == 0),
            rx.text(f"Page {TableState.page + 1} of {TableState.total_pages}"),
            rx.button("Next", on_click=TableState.next_page, is_disabled=TableState.page >= TableState.total_pages - 1),
            justify="center",
            margin_top="1em",
        ),
        width="100%",
    )
