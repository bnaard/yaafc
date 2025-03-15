import reflex as rx

# from yaafc.components.file_list import file_list
from yaafc.templates.template import template


@template(template="main", route="/404", title="YAAFC")
def not_found_404() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.text("Oops! Page Not Found", font_size="3rem"),
            rx.text(
                "It looks like the page you're looking for doesn't exist.",
                color="gray",
                font_size="2rem",
            ),
            rx.link(
                rx.button("Go to Homepage"),
                href="/",
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
