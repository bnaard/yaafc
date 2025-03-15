import reflex as rx

from yaafc.components.file_list import file_list
from yaafc.templates.template import template


@template(template="main", route="/files", title="YAAFC")
def files() -> rx.Component:
    return rx.box(
        file_list(),
        background_color=rx.Color("accent", 2),
        justify="center",
        padding="0em",
        margin="0em",
        height="100%",
        # flex_grow="1",
    )
