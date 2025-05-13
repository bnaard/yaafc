import reflex as rx

from yaafc.events.enhanced_event_watcher import enhanced_event_watcher
from yaafc.states.slotted_page import SlottedPageState
from yaafc.templates.template import template
from yaafc.ui.widgets.widget_stack import WidgetStack, widget_stack


class LayoutState(SlottedPageState):
    grid_rows: rx.Field[int] = rx.field(4)
    grid_columns: rx.Field[int] = rx.field(4)
    dropped_widgets: rx.Field[list[str]] = rx.field([])
    dropped_positions: rx.Field[list[tuple[int, int]]] = rx.field([])
    highlight_drop: rx.Field[tuple[int, int] | None] = rx.field(None)

    @rx.event
    def drop_widget(self, widget_name: str, grid_row: int, grid_col: int):
        self.dropped_widgets.append(widget_name)
        self.dropped_positions.append((grid_row, grid_col))

    @rx.event
    def set_highlight_drop(self, row: int, col: int):
        self.highlight_drop = (row, col)

    @rx.event
    def clear_highlight_drop(self):
        self.highlight_drop = None

    @rx.var
    def rows(self) -> str:
        return f"{self.grid_rows}"

    @rx.var
    def columns(self) -> str:
        return f"{self.grid_columns}"

    @rx.var
    def rows_range(self) -> list[int]:
        return list(range(self.grid_rows))

    @rx.var
    def columns_range(self) -> list[int]:
        return list(range(self.grid_columns))

    @rx.var
    def placed_widgets(self) -> list[tuple[str, int, int]]:
        # Returns a list of (widget_name, grid_row, grid_col)
        return [(w, pos[0], pos[1]) for w, pos in zip(self.dropped_widgets, self.dropped_positions)]

    @classmethod
    def grid_drop_area(cls, row: int, col: int) -> rx.Component:
        def handle_drop(ev):
            widget_name = getattr(ev, "dataTransfer", None) or getattr(ev, "data_transfer", None)
            return cls.drop_widget(widget_name, row, col)

        @rx.event
        def on_drag_over(self, ev):
            return self.set_highlight_drop(row, col)

        @rx.event
        def on_drag_leave(self, ev):
            return self.clear_highlight_drop()

        try:
            return enhanced_event_watcher(
                on_drag_over=on_drag_over.prevent_default,
                on_drag_leave=on_drag_leave,
                on_drop=handle_drop,
                children=[
                    rx.box(
                        width="100%",
                        height="100%",
                        style=rx.cond(
                            cls.highlight_drop == (row, col),
                            {"border": "2px solid #0070f3", "background": "#e6f0ff", "minHeight": "80px"},
                            {"border": "1px dashed #ccc", "minHeight": "80px"},
                        ),
                    )
                ],
            )
        except TypeError:
            # Fallback for test/mocked context: just return the box
            return rx.box(
                width="100%",
                height="100%",
                style={"border": "1px dashed #ccc", "minHeight": "80px"},
            )

    # Helper to render the grid with drop areas and placed widgets
    @classmethod
    def get_component(cls, *children, **props) -> rx.Component:
        def place_widget(row: int, col: int) -> rx.Component:
            # Check if a widget is placed here
            placed = None
            for wname, prow, pcol in props.get("placed_widgets", []):
                if prow == row and pcol == col:
                    placed = wname
                    break
            if placed:
                # Render the actual widget from WidgetStack
                widget_fn = WidgetStack._widget_create_funcs.get(placed)
                comp = widget_fn() if widget_fn else rx.text(f"Missing: {placed}")
                return rx.box(comp, style={"border": "1px solid #aaa", "minHeight": "80px"})
            else:
                # Render drop area
                return cls.grid_drop_area(row, col)

        return rx.grid(
            rx.foreach(cls.rows_range, lambda row: rx.foreach(cls.columns_range, lambda col: place_widget(row, col))),
            gap="1rem",
            columns=f"{props.get('columns', '4')}",
            rows=f"{props.get('rows', '4')}",
            justify="center",
            spacing="4",
            width="100%",
            height="100%",
        )


layout_state = LayoutState.create


@template(template="main", route="/layout", title="YAAFC")
def layout() -> rx.Component:
    WidgetStack.registerWidget(
        "A",
        lambda: rx.text("WidgetA"),
        description="This is widget A",
        icon="plus",
        grid_columns=1,
        grid_rows=1,
    )
    WidgetStack.registerWidget(
        "B",
        lambda: rx.text("WidgetB"),
        description="This is widget B",
        icon="sheet",
        grid_columns=1,
        grid_rows=1,
    )

    return rx.flex(
        widget_stack(),
        layout_state(),
        direction="row",
        spacing="4",
    )
