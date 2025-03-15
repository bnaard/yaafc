from datetime import datetime, timezone
from pathlib import Path
from typing import ClassVar, Union

import reflex as rx

from yaafc.utilities.humanbytes import HumanBytes


class FileListState(rx.State):
    current_directory: str = "/"

    visible_columns: ClassVar[list[dict[str : str | int]]] = [
        {
            "title": "Name",
            "type": "str",
            "width": 300,
        },
        {
            "title": "Size",
            "type": "str",
            "width": 300,
        },
        {
            "title": "Changed",
            "type": "str",
            "width": 300,
        },
    ]

    hidden_columns: ClassVar[list[dict[str : str | int]]] = [
        {
            "title": "Rights",
            "type": "str",
            "width": 300,
        },
        {
            "title": "Owner",
            "type": "str",
            "width": 300,
        },
        {
            "title": "Group",
            "type": "str",
            "width": 300,
        },
    ]

    @rx.var
    def data(self) -> list[list[str | int]]:
        new_data = []
        entries = sorted(Path(self.current_directory).glob("*"))
        directories = [entry for entry in entries if entry.is_dir()]
        files = [entry for entry in entries if not entry.is_dir()]
        for item in directories:
            new_entry = self._add_directory_entry(item)
            new_data.append(new_entry)
        for item in files:
            new_entry = self._add_directory_entry(item)
            new_data.append(new_entry)
        return new_data

    # def _clear_directory_entries(self ) -> None:
    #     self.data = []

    def _add_directory_entry(self, entry: Path) -> list[str | int]:
        new_entry = []
        for column in self.visible_columns:
            if column["title"] == "Name":
                if entry.is_dir():
                    new_entry.append("/" + entry.name)
                else:
                    new_entry.append(entry.name)

            elif column["title"] == "Size":
                if entry.exists():
                    if entry.is_dir():
                        new_entry.append("> SUB-DIR <")
                    else:
                        size = HumanBytes.format(entry.stat().st_size)
                        new_entry.append(str(size))
                else:
                    new_entry.append("--")

            elif column["title"] == "Changed":
                if entry.exists():
                    modified = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc)
                    new_entry.append(str(modified))
                else:
                    new_entry.append("--")

        return new_entry

    # @rx.event
    # def load_entries(self) -> None:
    #     # self._clear_directory_entries()
    #     for item in Path.iterdir(Path(self.current_directory)):
    #         self._add_directory_entry(item)
    #         print(item.name)

    def click_cell(self, pos):
        col, row = pos
        yield self.get_clicked_data(pos)

    def get_clicked_data(self, pos) -> str:
        self.clicked_data = f"Cell clicked: {pos}"


def show_directory_table_entry(entry: list[str | int]) -> rx.Component:
    def show_cell(content: str, min_width: Union[str, list[str]], max_width: Union[str, list[str]]) -> rx.Component:
        return (
            rx.table.cell(
                content,
                border_right="solid",
                border_right_color=rx.color("accent", 4),
                border_right_width="1px",
                border_bottom="solid",
                border_bottom_color=rx.color("accent", 4),
                border_bottom_width="1px",
                height="1em",
                padding="5px",
                padding_left="10px",
                min_width=min_width,
                max_width=max_width,
            ),
        )

    return rx.table.row(
        show_cell(entry[0], "8em", "64em"),
        show_cell(entry[1], "4em", "12em"),
        show_cell(entry[2], "4em", "12em"),
        show_cell("ooo", "4em", "12em"),
        # arrow.get(entry[2]).format('YYYY-MM-DD'),
        # arrow.get(entry[2]).format('HH:mm:ss ZZ'),
    )


def show_directory_table_header() -> rx.Component:
    def show_header_cell(content: str) -> rx.Component:
        return rx.table.column_header_cell(
            content,
            border_right="solid",
            border_right_color=rx.color("accent", 4),
            border_right_width="1px",
            border_bottom="solid",
            border_bottom_color=rx.color("accent", 4),
            border_bottom_width="1px",
            background_color=rx.color("accent", 3),
            style={"position": "sticky", "top": "0"},
        )

    return rx.table.header(
        rx.table.row(
            show_header_cell("Name"),
            show_header_cell("Size"),
            show_header_cell("Changed Date"),
            show_header_cell("Change Time"),
        ),
    )


def show_directory_table():
    return rx.table.root(
        show_directory_table_header(),
        rx.table.body(
            rx.foreach(FileListState.data, show_directory_table_entry),
            # style={"max-height": "100px", "overflow-y": "auto"},
        ),
        width="100%",
        height="100%",
        style={"position": "relative"},
    )


def show_file_list_header() -> rx.Component:
    return rx.hstack(
        rx.form.root(
            rx.form.field(
                rx.input(
                    name="current_directory",
                    type="text",
                    placeholder="Current directory...",
                    value=FileListState.current_directory,
                    # on_change=TextfieldControlled.set_text,
                ),
                padding="0em",
                margin="0em",
                width="100%",
            ),
            on_submit=lambda form_data: rx.window_alert(form_data.to_string()),
        ),
        rx.button(
            rx.icon(tag="search", size=20),
            border="solid",
            border_width="1px",
            border_color=rx.color("accent", 8),
        ),
        rx.button(
            rx.icon(tag="filter", size=20),
            border="solid",
            border_width="1px",
            border_color=rx.color("accent", 8),
        ),
        rx.button(
            rx.icon(tag="settings", size=20),
            border="solid",
            border_width="1px",
            border_color=rx.color("accent", 8),
        ),
        width="100%",
        border="solid",
        border_width="1px",
        border_color=rx.color("accent", 8),
        background_color=rx.color("accent", 1),
        padding="0em",
        margin="0em",
        spacing="0",
    )


def file_list() -> rx.Component:
    return (
        rx.flex(
            rx.box(
                show_file_list_header(),
            ),
            rx.box(
                show_directory_table(),
                style={"height": "calc(100% - 2.6em)"},
            ),
            direction="column",
            border="solid",
            border_width="1px",
            border_color=rx.color("accent", 8),
            background_color=rx.color("accent", 1),
            height="100%",
            padding="0em",
            margin="0em",
        ),
    )


# import reflex as rx

# BATCH_SIZE = 15

# class State(rx.State):
#     # Initialize table data
#     table_data: list[dict] = [{"id": i, "name": f"Item {i}"} for i in range(BATCH_SIZE)]

#     def load_more_data(self, entry):
#         # Add more rows when scrolled
#         start = len(self.table_data)
#         new_data = [{"id": i, "name": f"Item {i}"} for i in range(start, start + BATCH_SIZE)]
#         self.table_data.extend(new_data)

# def index():
#     return rx.scroll_area(
#         rx.el.table(
#             rx.el.thead(
#                 rx.el.tr(
#                     rx.el.th("ID"),
#                     rx.el.th("Name"),
#                 )
#             ),
#             rx.el.tbody(
#                 rx.foreach(
#                     State.table_data,
#                     lambda row: rx.el.tr(
#                         rx.el.td(row["id"]),
#                         rx.el.td(row["name"]),
#                     )
#                 ),
#             ),
#             # Add intersection observer at bottom of table
#             IntersectionObserver.create(
#                 "",  # Empty content for observer
#                 root="#table-scroll",
#                 root_margin="0px",
#                 threshold=0.9,
#                 on_intersect=State.load_more_data,
#             ),
#         ),
#         id="table-scroll",
#         height="75vh",
#         width="100%",
#     )


# rx.vstack(
#     rx.card(
#         "Card",
#         width="100%",
#         height="260px",
#     ),
#     grid_column="span 2",  # This makes the card span 2 columns
# )

# rx.grid(
#     rx.foreach(
#         rx.Var.range(12),
#         lambda i: rx.card(f"Card {i + 1}", height="10vh"),
#     ),
#     gap="1rem",
#     grid_template_columns=[
#         "1fr",                # 1 column for mobile
#         "repeat(2, 1fr)",     # 2 columns for tablet
#         "repeat(2, 1fr)",     # 2 columns for small desktop
#         "repeat(3, 1fr)",     # 3 columns for medium desktop
#         "repeat(4, 1fr)",     # 4 columns for large desktop
#     ],
#     width="100%",
# )
