import reflex as rx

from yaafc.events import EnhancedEventWatcher, MouseEvent


class CardComponent(rx.ComponentState):
    """A StateComponent-based card for the layout grid."""

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
        return super().create(*children, **props)

    @classmethod
    def get_component(cls, **props) -> rx.Component:
        return rx.card(
            EnhancedEventWatcher.create(
                rx.box(
                    rx.vstack(
                        rx.mobile_only(
                            rx.icon("plus", color=rx.color("accent", 11), size=25),
                        ),
                        rx.tablet_and_desktop(
                            rx.icon("plus", color=rx.color("accent", 11), size=50),
                        ),
                        align="center",
                        justify="center",
                        height="100%",
                    ),
                    height="100%",
                    width="100%",
                ),
                on_mouse_down=cls.handle_mouse_down,
            ),
            grid_row=f"span {cls.row_span}",
            grid_column=f"span {cls.col_span}",
            style={
                "_hover": {
                    "filter": "grayscale(50%) brightness(120%) opacity(80%)",
                }
            },
            **props,
        )


card_component = CardComponent.create
