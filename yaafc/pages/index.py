import reflex as rx

from yaafc.components.file_list import file_list
from yaafc.templates.template import template


@template(template="main", route="/", title="YAAFC")
def index() -> rx.Component:
    return rx.vstack(
        file_list(),
        background_color=rx.Color("accent", 2),
        justify="center",
        height="90vh",
        padding="0em",
        margin="0em",
    )
