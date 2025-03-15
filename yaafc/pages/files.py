import reflex as rx

from yaafc.components.native_file_list import native_file_list
from yaafc.templates.template import template


@template(template="main", route="/files", title="YAAFC")
def files() -> rx.Component:
    return rx.box(
        native_file_list(),
        background_color=rx.Color("accent", 2),
        justify="center",
        padding="0em",
        margin="0em",
        height="100%",
        # flex_grow="1",
    )
