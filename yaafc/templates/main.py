from typing import Callable

import reflex as rx

from yaafc.components.header import header
from yaafc.components.sidebar import sidebar


def main_template(page_content: Callable[[], rx.Component]) -> rx.Component:
    return rx.hstack(
        sidebar(),
        rx.vstack(header(), page_content(), padding="0em", margin="0em", spacing="0", text_align="left"),
        padding="0em",
        margin="0em",
        spacing="0",
        width=["520px", "768px", "1024px", "1280px", "1640px"],
        # max_width=["30em", "48em",  "62em", "80em", "96em"],
    )


# ["520px", "768px", "1024px", "1280px", "1640px"]})
