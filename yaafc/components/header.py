import reflex as rx


def header():
    return rx.flex(
        rx.heading("YAAFC", size="6", color=rx.color("accent", 11)),
        rx.spacer(),
        rx.hstack(
            rx.link(
                "Docs",
                href="/docs",
            ),
            rx.color_mode.button(color=rx.color("accent", 11)),
            padding_right="1em",
            align="center",
        ),
        flex_direction=["column", "column", "row", "row", "row"],
        spacing="1",
        width="100%",
        min_height="3em",
        align="center",
        margin="0em",
        padding="0em",
    )
