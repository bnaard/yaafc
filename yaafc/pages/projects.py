import reflex as rx

import yaafc.ui as yui
from yaafc.templates.template import template


@template(template="main", route="/projects", title="YAAFC")
def projects() -> rx.Component:
    return rx.box(
        yui.table(),
        background_color=rx.Color("accent", 2),
        justify="center",
        padding="0em",
        margin="0em",
        height="100%",
    )
