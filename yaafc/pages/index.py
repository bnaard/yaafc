import reflex as rx

# from yaafc.components.file_list import file_list
from yaafc.templates.template import template


@template(template="main", route="/", title="YAAFC")
def index() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.text("Imagine", font_size="3rem"),
            rx.text(
                "a dashboard for the target system",
                color="gray",
                font_size="2rem",
            ),
            spacing="4",
            direction="column",
            text_align="center",
            width="100%",
        ),
        background_color=rx.Color("accent", 2),
        justify="center",
        height="90vh",
        padding="0em",
        margin="0em",
    )
