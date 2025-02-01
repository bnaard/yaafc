import reflex as rx


def header():
    return rx.flex(
        rx.color_mode_cond(
            rx.image(
                src="/yaafc_logo.svg",
                height="2em",
                width="2.7em",
                justify="center",
                text_align="center",
                padding_x="0.2em",
                padding_top="0.2em",
                padding_bottom="0em",
                margin_bottom="0em",
            ),
            rx.image(
                src="/yaafc_logo_inv.svg",
                height="2em",
                width="2.7em",
                justify="center",
                text_align="center",
                padding_x="0.2em",
                padding_top="0.2em",
                padding_bottom="0em",
                margin_bottom="0em",
            ),
        ),
        rx.heading("YAAFC", size="5", color=rx.color("accent", 11)),
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
        flex_direction=["column", "column", "row"],
        spacing="2",
        width="100%",
        align="center",
        margin="0em",
        padding="0em",
    )
