import reflex as rx

from yaafc.components.native_file_list import native_file_list
from yaafc.templates.template import template


@template(template="main", route="/files", title="YAAFC")
def files() -> rx.Component:
    return rx.vstack(
        native_file_list(),
        background_color=rx.Color("accent", 2),
        justify="center",
        height="90vh",
        padding="0em",
        margin="0em",
    )
