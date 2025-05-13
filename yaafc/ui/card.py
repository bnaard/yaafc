import reflex as rx

from yaafc.events import EnhancedEventWatcher, MouseEvent


class CardComponent(rx.ComponentState):
    """A StateComponent-based card for the layout grid."""

    grid_row: int = 1
    grid_column: int = 1
    row_span: int = 1
    col_span: int = 1

    @rx.event
    def handle_mouse_down(self, event: MouseEvent):
        """Handle mouse down event."""
        if event.altKey:
            self.set_row_span(2) if self.row_span == 1 else self.set_row_span(1)
        else:
            self.col_span = 2 if self.col_span == 1 else 1

    @classmethod
    def create(cls, *children, **props) -> rx.Component:
        """Create a card component with mouse down event handling."""
        cls.__fields__["row_span"].default = props.pop("row_span", cls.__fields__["row_span"].default)
        cls.__fields__["col_span"].default = props.pop("col_span", cls.__fields__["col_span"].default)
        cls.__fields__["grid_row"].default = props.pop("grid_row", cls.__fields__["grid_row"].default)
        cls.__fields__["grid_column"].default = props.pop("grid_column", cls.__fields__["grid_column"].default)
        return super().create(*children, **props)

    @classmethod
    def get_component(cls, *children, **props) -> rx.Component:
        user_style = props.pop("style", {}) or {}
        default_style = {
            "_hover": {
                "filter": "grayscale(50%) brightness(120%) opacity(80%)",
            }
        }
        merged_style = {**default_style, **user_style}

        return rx.card(
            EnhancedEventWatcher.create(
                rx.flex(
                    rx.vstack(
                        rx.mobile_only(
                            rx.icon("plus", color=rx.color("accent", 11), size=25),
                        ),
                        rx.tablet_and_desktop(
                            rx.icon("plus", color=rx.color("accent", 11), size=50),
                        ),
                    ),
                    rx.box(
                        *children,
                    ),
                    spacing="2",
                    direction="row",
                    align="center",
                    justify="start",
                    wrap="nowrap",
                ),
                on_mouse_down=cls.handle_mouse_down,
            ),
            grid_row=f"{cls.grid_row} / span {cls.row_span}",
            grid_column=f"{cls.grid_column} / span {cls.col_span}",
            style=merged_style,
            **props,
        )


card_component = CardComponent.create
