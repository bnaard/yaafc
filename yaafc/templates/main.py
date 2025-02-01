from typing import Callable

import reflex as rx

from yaafc.components.header import header
from yaafc.components.sidebar import sidebar


def main_template(page_content: Callable[[], rx.Component]) -> rx.Component:
    return rx.vstack(
        header(),
        rx.hstack(sidebar(), page_content(), padding="0em", margin="0em", spacing="0", text_align="left"),
        padding="0em",
        margin="0em",
    )
