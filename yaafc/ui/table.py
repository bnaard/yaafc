from typing import Any

import polars as pl
import reflex as rx


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

    def test_update(self):
        self._df = self._df.update(pl.DataFrame({"Age": [99, None, 42]}))


def table():
    columns = TableState.columns
    rows = TableState.page_rows

    return rx.box(
        rx.box(
            rx.table.root(
                rx.table.header(rx.table.row(rx.foreach(columns, lambda col: rx.table.column_header_cell(col)))),
                rx.table.body(
                    rx.foreach(
                        rows,
                        lambda row: rx.table.row(
                            rx.foreach(row, lambda cell: rx.table.cell(cell)),
                        ),
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
            rx.button("Test Update", on_click=TableState.test_update),
            justify="center",
            margin_top="1em",
        ),
        width="100%",
    )


# class TableHeaderCell(rx.Component):
#     @classmethod
#     def create(cls, *children, **props) -> rx.Component:
#         return rx.table.column_header_cell(
#             *children,
#             border_right="solid",
#             border_right_color=rx.color("accent", 4),
#             border_right_width="1px",
#             border_bottom="solid",
#             border_bottom_color=rx.color("accent", 4),
#             border_bottom_width="1px",
#             background_color=rx.color("accent", 3),
#             style={"position": "sticky", "top": "0"},
#             **props,
#         )


# table_header_cell = TableHeaderCell.create


# class TableHeader(rx.Component):
#     @classmethod
#     def create(cls, labels: list[rx.Component], **props) -> rx.Component:  # , *children,
#         return rx.table.header(
#             rx.table.row(
#                 rx.foreach(
#                     [rx.text("Name"), rx.text("Size"), rx.text("Changed Date"), rx.text("Change Time")],
#                     lambda component: table_header_cell(component),
#                 ),
#                 # rx.foreach(labels, lambda component: table_header_cell(component) ),
#                 **props,
#             ),
#         )


# table_header = TableHeader.create


# class Table(rx.ComponentState):
#     _data: pl.DataFrame = pl.DataFrame({
#         "name": ["Alice Archer", "Ben Brown", "Chloe Cooper", "Daniel Donovan"],
#         "Birthdate": [
#             dt.date(1997, 1, 10),
#             dt.date(1985, 2, 15),
#             dt.date(1983, 3, 22),
#             dt.date(1981, 4, 30),
#         ],
#         "weight": [57.9, 72.5, 53.6, 83.1],  # (kg)
#         "height": [1.56, 1.77, 1.65, 1.75],  # (m)
#     })

#     @classmethod
#     def create_table_header(cls, labels: list[rx.Component], **props) -> rx.Component:  # , *children,
#         return rx.table.header(
#             rx.table.row(
#                 # rx.foreach([rx.text("Name"), rx.text("Size"), rx.text("Changed Date"), rx.text("Change Time")], lambda component: table_header_cell(component) ),
#                 # rx.foreach(labels, lambda component: table_header_cell(component) ),
#                 rx.foreach(labels, lambda c: table_header_cell(c)),
#                 **props,
#             ),
#         )

#     # @rx.var(cache=True)
#     # def get_header_labels(self) -> list[str]:
#     #     return list(self._data.columns)

#     @rx.var(cache=False)
#     def get_header_labels(self) -> list[rx.Component]:
#         return [rx.button("Button 1"), rx.text("Some text"), rx.heading("A heading")]

#     # @rx.var(cache=True)
#     # def get_header_types(self) -> list[str]:
#     #     return list(self._data.dtypes)

#     # if include_types:
#     #     labels = zip(self._data.columns, self._data.dtypes)
#     #     return [ rx.fragment( rx.text(str(x[0])), rx.text(" (" + str(x[1]) + ")", color=yui.color(yui.GRAY)) ) for x in labels ]
#     # else:
#     #     return [rx.text("xxx"), rx.text("vvv")]
#     # [ rx.text( str(x) ) for x in self._data.columns]
#     # labels = list( self._data.columns) if not include_types else [ str(x[0]) + " (" + str(x[1]) + ")" for x in zip(self._data.columns, self._data.dtypes) ]
#     # return labels

#     # @rx.var(cache=True)
#     # def page(self) -> list[int]:
#     #     return [
#     #         int(x)  # explicit cast to int
#     #         for x in self._backend[self.offset : self.offset + self.limit]
#     #     ]

#     @classmethod
#     def get_component(cls, *children, **props) -> rx.Component:
#         props.setdefault("height", "100%")
#         props.setdefault("padding", "0.3em")
#         props.setdefault("margin", "0em")
#         props.setdefault("spacing", "0")
#         props.setdefault("style", {"position": "sticky", "top": "0"})
#         props.setdefault("direction", "column")

#         # return rx.table.root(
#         #     cls.create_table_header(labels=cls.get_header_labels),
#         #     # rx.table.body(
#         #     #     rx.foreach(FileListState.data, show_directory_table_entry),
#         #     # ),
#         #     width="100%",
#         #     height="100%",
#         #     style={"position": "relative"},
#         # )

#         return rx.flex(
#             rx.box("Table", height="1.2em", backhround=yui.color(yui.WARNING)),
#             **props,
#         )


# table = Table.create
