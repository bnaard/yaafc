from dataclasses import dataclass
from typing import Callable, ClassVar

import reflex as rx


@dataclass
class WidgetMeta:
    name: str
    description: str = ""
    icon: str = ""
    grid_columns: int = 1
    grid_rows: int = 1


class WidgetStack(rx.ComponentState):
    """A stack of widgets, each registered by name, description, icon, and size. Widget create functions are stored separately."""

    widgets: ClassVar[list[WidgetMeta]] = []
    _widget_create_funcs: ClassVar[dict[str, Callable[[], rx.Component]]] = {}

    @classmethod
    def registerWidget(
        cls,
        name: str,
        create_fn: Callable[[], rx.Component],
        description: str = "",
        icon: str = "",
        grid_columns: int = 1,
        grid_rows: int = 1,
    ):
        """Register a widget by name, create function, description, icon, and size. Overwrites if name exists."""
        if not callable(create_fn):
            raise TypeError
        # Remove any existing widget with the same name
        cls.widgets = [w for w in cls.widgets if w.name != name]
        cls.widgets.append(
            WidgetMeta(
                name=name,
                description=description,
                icon=icon,
                grid_columns=grid_columns,
                grid_rows=grid_rows,
            )
        )
        cls._widget_create_funcs[name] = create_fn

    @staticmethod
    def widget_repr_component(widget: WidgetMeta, **props) -> rx.Component:
        """Return a draggable component representing a widget: icon left, name+desc right."""
        user_style = props.pop("style", {}) or {}
        default_style = {
            "_hover": {
                "filter": "grayscale(50%) brightness(120%) opacity(80%)",
            }
        }
        merged_style = {**default_style, **user_style}

        return rx.card(
            rx.hstack(
                rx.icon(rx.cond(widget.icon, widget.icon, "plus"), size=24, color=rx.color("accent", 8)),
                rx.vstack(
                    rx.heading(widget.name, size="4"),
                    rx.text(rx.cond(widget.description, widget.description, ""), size="2", color=rx.color("gray", 10)),
                    spacing="1",
                ),
                spacing="2",
                align="center",
                width="100%",
            ),
            draggable=True,
            width="100%",
            style=merged_style,
            # Optionally, add drag event handlers here if needed:
            # on_drag_start=..., on_drag_end=...
        )

    @classmethod
    def list_registered_widgets(cls) -> rx.Component:
        """Return a list of all registered widgets using widget_repr_component, using rx.foreach."""
        return rx.vstack(
            rx.foreach(cls.widgets, lambda widget: cls.widget_repr_component(widget)),
            spacing="2",
            width="100%",
            align="center",
            justify="center",
        )

    @classmethod
    def get_component(cls, *children, **props) -> rx.Component:
        return rx.card(
            cls.list_registered_widgets(),
            width=props.get("width", "15vw"),
            background_color=props.get("background_color", rx.color("accent", 2)),
            **props,
        )


widget_stack = WidgetStack.create
