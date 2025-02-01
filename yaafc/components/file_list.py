from datetime import datetime, timezone
from pathlib import Path
from typing import ClassVar

import reflex as rx

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


def get_data_editor_theme(dark: bool = False):
    return {
        "accentColor": rgba_hex("accent", 10, dark=dark),  # "#8c96ff"
        "accentLight": rgba_hex("accent", 10, dark=dark, alpha=True),
        "accentFg": rgba_hex("accent", 2, dark=dark),
        "textDark": rgba_hex("accent", 12, dark=dark),  # "#ff0000", #"#ffffff",
        "textMedium": rgba_hex("accent", 11, dark=dark),  # "#b8b8b8",
        "textLight": rgba_hex("accent", 11, dark=dark, alpha=True),  # "#a0a0a0",
        "textBubble": rgba_hex("accent", 12, dark=dark),  # "#ffffff",
        "bgIconHeader": rgba_hex("accent", 1, dark=dark),  # "#b8b8b8",
        "fgIconHeader": rgba_hex("gray", 1, dark=dark),  # "#000000",
        "textHeader": rgba_hex("accent", 11, dark=dark),  # "#a1a1a1",
        "textHeaderSelected": rgba_hex("gray", 12, dark=dark),  # "#000000",
        "textGroupHeader": rgba_hex("gray", 11, dark=dark),  # "#000000",
        "bgCell": rgba_hex("accent", 1, dark=dark),  # "#16161b",
        "bgCellMedium": rgba_hex("accent", 2, dark=dark),  # "#202027",
        "bgHeader": rgba_hex("accent", 1, dark=dark),  # "#212121",
        "bgHeaderHasFocus": rgba_hex("gray", 1, dark=dark),  # "#474747",
        "bgHeaderHovered": rgba_hex("gray", 2, dark=dark),  # "#404040",
        "bgBubble": rgba_hex("gray", 1, dark=dark),  # "#212121",
        "bgBubbleSelected": rgba_hex("gray", 2, dark=dark),  # "#000000",
        "bgSearchResult": rgba_hex("accent", 2, dark=dark),  # "#423c24",
        "borderColor": rgba_hex("accent", 7, dark=dark),  # "rgba(225,225,225,0.2)",
        "drilldownBorder": rgba_hex("accent", 6, dark=dark),  # "rgba(225,225,225,0.4)",
        "linkColor": rgba_hex("gray", 11, dark=dark),  # "#4F5DFF",
        "cellHorizontalPadding": 10,
        "cellVerticalPadding": 2,
        "lineHeight": 10,
        "headerFontStyle": "bold 14px",
        "baseFontStyle": "13px",
        "fontFamily": "Inter, Roboto, -apple-system, BlinkMacSystemFont, avenir next, avenir, segoe ui, helvetica neue, helvetica, Ubuntu, noto, arial, sans-serif",
    }


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
