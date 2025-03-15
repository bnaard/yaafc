from datetime import datetime, timezone
from pathlib import Path
from typing import ClassVar

import reflex as rx
from reflex.components.datadisplay.dataeditor import (
    DataEditorTheme,
)

from yaafc.utilities.colors import rgba_hex
from yaafc.utilities.humanbytes import HumanBytes


class DataEditorState_HP(rx.State):
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

    # data: ClassVar[list[list[str | int]]] = [
    #     [
    #         "noname",
    #         "12345",
    #         "2022-01-01",
    #     ]
    # ]

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


def get_data_editor_theme(dark: bool = False) -> DataEditorTheme:
    theme = DataEditorTheme()
    theme.accent_color = rgba_hex("accent", 10, dark=dark)
    theme.accent_fg = rgba_hex("accent", 2, dark=dark)
    theme.accent_light = rgba_hex("accent", 10, dark=dark, alpha=True)
    theme.base_font_style = "13px"
    theme.bg_bubble = rgba_hex("gray", 1, dark=dark)
    theme.bg_bubble_selected = rgba_hex("gray", 2, dark=dark)
    theme.bg_cell = rgba_hex("accent", 1, dark=dark)
    theme.bg_cell_medium = rgba_hex("accent", 2, dark=dark)
    theme.bg_header = rgba_hex("accent", 1, dark=dark)
    theme.bg_header_has_focus = rgba_hex("gray", 1, dark=dark)
    theme.bg_header_hovered = rgba_hex("gray", 2, dark=dark)
    theme.bg_icon_header = rgba_hex("accent", 1, dark=dark)
    theme.bg_search_result = rgba_hex("accent", 2, dark=dark)
    theme.border_color = rgba_hex("accent", 7, dark=dark)
    theme.cell_horizontal_padding = 10
    theme.cell_vertical_padding = 2
    theme.drilldown_border = rgba_hex("accent", 6, dark=dark)
    theme.editor_font_size = "13px"
    theme.fg_icon_header = rgba_hex("gray", 1, dark=dark)
    theme.font_family = "Inter, Roboto, -apple-system, BlinkMacSystemFont, avenir next, avenir, segoe ui, helvetica neue, helvetica, Ubuntu, noto, arial, sans-serif"
    theme.header_bottom_border_color = rgba_hex("accent", 8, dark=dark)
    theme.header_font_style = "bold 14px"
    theme.horizontal_border_color = rgba_hex("accent", 8, dark=dark)
    theme.line_height = "10"
    theme.link_color = rgba_hex("gray", 11, dark=dark)
    theme.text_bubble = rgba_hex("accent", 12, dark=dark)
    theme.text_dark = rgba_hex("accent", 12, dark=dark)
    theme.text_group_header = rgba_hex("gray", 11, dark=dark)
    theme.text_header = rgba_hex("accent", 11, dark=dark)
    theme.text_header_selected = rgba_hex("gray", 12, dark=dark)
    theme.text_light = rgba_hex("accent", 11, dark=dark, alpha=True)
    theme.text_medium = rgba_hex("accent", 11, dark=dark)
    return theme


def file_list() -> rx.Component:
    return (
        rx.flex(
            rx.vstack(
                rx.hstack(
                    rx.form.root(
                        rx.form.field(
                            rx.input(
                                name="current_directory",
                                type="text",
                                placeholder="Current directory...",
                                value=DataEditorState_HP.current_directory,
                                # on_change=TextfieldControlled.set_text,
                                flex="1",
                            ),
                        ),
                        on_submit=lambda form_data: rx.window_alert(form_data.to_string()),
                    ),
                    rx.button(rx.icon(tag="settings", size=20)),
                    width="100%",
                    border="solid",
                    border_width="1px",
                    border_color=rx.color("accent", 8),
                    background_color=rx.color("accent", 1),
                    padding="0em",
                    margin="0em",
                ),
                rx.data_editor(
                    columns=DataEditorState_HP.visible_columns,
                    data=DataEditorState_HP.data,
                    # on_cell_clicked=DataEditorState_HP.click_cell,
                    theme=rx.color_mode_cond(light=get_data_editor_theme(), dark=get_data_editor_theme(dark=True)),
                    # on_mount=DataEditorState_HP.load_entries,
                ),
            ),
            flex_direction="column",
            border="solid",
            border_width="1px",
            border_color=rx.color("accent", 8),
            background_color=rx.color("accent", 1),
            height="100%",
            padding="0em",
            margin="0em",
        ),
    )
