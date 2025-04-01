from typing import Callable

import reflex as rx

# from yaafc.components.sidebar import sidebar
import yaafc.ui as yui
from yaafc.components.header import header


def main_template(page_content: Callable[[], rx.Component]) -> rx.Component:
    return rx.flex(
        rx.box(
            yui.sidebar(),
            height="100%",
            width="3em",
        ),
        rx.box(
            rx.flex(
                rx.box(
                    header(),
                    height="3em",
                    width="100%",
                ),
                rx.box(page_content(), style={"height": "calc(100vh - 3em)"}),
                width="100%",
                height="100%",
                direction="column",
                flex_direction=["column", "column", "column", "column", "column"],
            ),
            height="100%",
            flex_grow="1",
        ),
        padding="0em",
        margin="0em",
        spacing="0",
        text_align="left",
        width=["100vw", "100vw", "100vw", "97vw", "97vw"],
        height="100vh",
        direction="row",
        flex_direction=["row", "row", "row", "row", "row"],
    )


# ["520px", "768px", "1024px", "1280px", "1640px"]})
# max_width=["30em", "48em",  "62em", "80em", "96em"],
