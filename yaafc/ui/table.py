from typing import Any

import polars as pl
import reflex as rx
from reflex.vars import ArrayVar
from reflex_intersection_observer import intersection_observer

import yaafc.ui as yui
from yaafc.states.pages_selection import PagesSelectionState


class TableComponent(rx.ComponentState):
    _df = pl.DataFrame({
        "Index": list(range(1, 61)),
        "Name": [
            "Alice",
            "Bob",
            "Charlie",
            "David",
            "Eve",
            "Frank",
            "Grace",
            "Heidi",
            "Ivan",
            "Judy",
            "Karl",
            "Laura",
            "Mallory",
            "Niaj",
            "Olivia",
            "Peggy",
            "Quentin",
            "Rupert",
            "Sybil",
            "Trent",
            "Uma",
            "Victor",
            "Wendy",
            "Xander",
            "Yvonne",
            "Zach",
            "Aaron",
            "Bianca",
            "Carter",
            "Diana",
            "Ethan",
            "Fiona",
            "Gavin",
            "Hannah",
            "Isabel",
            "Jonas",
            "Kylie",
            "Liam",
            "Mona",
            "Nolan",
            "Opal",
            "Paul",
            "Quincy",
            "Rita",
            "Sam",
            "Tina",
            "Ursula",
            "Vince",
            "Will",
            "Xenia",
            "Yara",
            "Zane",
            "Ava",
            "Ben",
            "Clara",
            "Derek",
            "Elena",
            "Felix",
            "Gina",
            "Henry",
        ],
        "Age": [
            25,
            30,
            35,
            28,
            22,
            40,
            31,
            29,
            27,
            33,
            26,
            32,
            38,
            24,
            21,
            41,
            34,
            28,
            36,
            39,
            23,
            37,
            29,
            31,
            35,
            30,
            27,
            33,
            25,
            32,
            28,
            34,
            26,
            38,
            24,
            40,
            29,
            31,
            37,
            22,
            39,
            23,
            36,
            35,
            27,
            33,
            25,
            32,
            28,
            34,
            26,
            38,
            24,
            40,
            29,
            31,
            37,
            22,
            39,
            23,
        ],
        "City": [
            "NY",
            "LA",
            "Chicago",
            "Boston",
            "Miami",
            "Dallas",
            "Seattle",
            "Denver",
            "Austin",
            "SF",
            "Houston",
            "Phoenix",
            "Portland",
            "Atlanta",
            "Orlando",
            "Detroit",
            "Baltimore",
            "Cleveland",
            "Columbus",
            "Charlotte",
            "San Diego",
            "San Jose",
            "Jacksonville",
            "Indianapolis",
            "Fort Worth",
            "El Paso",
            "Memphis",
            "Nashville",
            "Louisville",
            "Milwaukee",
            "Albuquerque",
            "Tucson",
            "Fresno",
            "Sacramento",
            "Kansas City",
            "Mesa",
            "Omaha",
            "Colorado Springs",
            "Raleigh",
            "Long Beach",
            "Virginia Beach",
            "Oakland",
            "Minneapolis",
            "Tulsa",
            "Arlington",
            "Tampa",
            "New Orleans",
            "Wichita",
            "Bakersfield",
            "Aurora",
            "Anaheim",
            "Honolulu",
            "Santa Ana",
            "Riverside",
            "Corpus Christi",
            "Lexington",
            "Stockton",
            "Henderson",
            "Saint Paul",
            "St. Louis",
        ],
    })

    rows_loaded: int = 20
    load_batch_size: int = 5
    assigned_page_slot: int | None = None
    active_page_slot: int | None = None

    def get_client_rows_loaded_count(self):
        return [
            rx.call_script(
                "window.rows_loaded_count",
                callback=self.set_rows_loaded,
            ),
        ]

    @rx.var
    def columns(self) -> list[str]:
        return self._df.columns

    @rx.var
    def visible_rows(self) -> list[tuple[Any, ...]]:
        self.get_client_rows_loaded_count()
        return self._df.rows()[: self.rows_loaded]

    @rx.var
    def has_more(self) -> bool:
        return self.rows_loaded < self._df.height

    def set_rows_loaded(self, count: int):
        self.rows_loaded = min(count, self._df.height)

    def load_more_rows(self):
        if self.has_more:
            self.rows_loaded = min(self.rows_loaded + self.load_batch_size, self._df.height)

    def set_page_slot(self, slot: int):
        self.assigned_page_slot = slot

    def set_page_id(self, page_id: str):
        self.page_id = page_id

    @classmethod
    def table_header_cell(cls, *children, **props) -> rx.Component:
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

    @classmethod
    def table_header(cls, columns: ArrayVar[list[str]]) -> rx.Component:
        return rx.table.header(
            rx.table.row(rx.foreach(columns, lambda col: TableComponent.table_header_cell(col))),
        )

    @classmethod
    def table_row_cell(cls, *children, **props) -> rx.Component:
        return rx.table.cell(
            *children,
            border_bottom="solid",
            border_bottom_color=rx.color("accent", 4),
            border_bottom_width="1px",
            background_color=rx.color("accent", 2),
            **props,
        )

    @classmethod
    def table_row(cls, row: ArrayVar[tuple[Any, ...]], **props) -> rx.Component:
        return rx.table.row(rx.foreach(row, lambda cell: cls.table_row_cell(cell)), **props)

    @classmethod
    def get_component(cls, page_id: str, slot_id: int, *children, **props) -> rx.Component:
        columns = cls.columns
        rows = cls.visible_rows
        # cls.__fields__["assigned_page_slot"].default = props.pop("assigned_page_slot", cls.assigned_page_slot)
        # cls.__fields__["page_id"].default = props.pop("page_id", cls.page_id)
        # cls.__fields__["page_state"].default = props.pop("page_state", cls.page_state)

        js_code = """
        function updateRowsLoaded() {
            const tableHeight = window.innerHeight;
            const rowHeight = 30;
            const visibleRows = Math.floor(tableHeight / rowHeight);
            window.rows_loaded_count = visibleRows;
        }
        window.addEventListener('resize', updateRowsLoaded);
        updateRowsLoaded();
        """

        load_more_observer = intersection_observer(
            on_intersect=cls.load_more_rows,
            once=False,
            disabled=~cls.has_more,
            style={"height": "1px"},
            client_only=True,
        )

        # is_active = Settings.active_widget == cls.widget_id
        active_id_style = {
            "border": "3px solid",
            "borderColor": rx.color("accent", 8),
            "borderRadius": "8px",
            "boxShadow": f"0 0 8px 2px {rx.color('accent', 5)}",
        }

        return rx.vstack(
            rx.script(js_code),
            rx.text(
                "page_slot=",
                background=yui.color(yui.INFO),
                on_click=lambda: PagesSelectionState.set_active_slot_id(page_id, slot_id + 1),
            ),
            rx.box(
                rx.table.root(
                    cls.table_header(columns),
                    rx.table.body(
                        rx.foreach(rows, lambda row: cls.table_row(row)),
                        rx.cond(
                            cls.has_more,
                            rx.table.row(
                                cls.table_row_cell("Loading...", load_more_observer),
                            ),
                            None,
                        ),
                    ),
                    width="100%",
                    style={"minWidth": "600px"},
                    sticky_header=True,
                    height="90vh",
                    overflow_y="auto",
                ),
                width="100%",
                style=rx.cond((PagesSelectionState.active_slot_ids.get(page_id) == slot_id), active_id_style, {}),
                on_click=lambda: PagesSelectionState.set_active_slot_id(page_id, slot_id),
            ),
        )


table = TableComponent.create
