import reflex as rx

import yaafc.ui as yui
from yaafc.config import menus


class Header(rx.Component):
    @classmethod
    def create(cls, *children, **props) -> rx.Component:
        return rx.flex(
            rx.heading("YAAFC", size="6", color=yui.color(yui.ACCENT), padding_left="0.2em"),
            rx.spacer(),
            rx.hstack(
                rx.foreach(menus.header, lambda item: rx.link(item["label"], href=item["href"])),
                rx.color_mode.button(color=yui.color(yui.ACCENT)),
                padding_right="1em",
                align="center",
            ),
            *children,
            flex_direction=["column", "column", "row", "row", "row"],
            spacing="1",
            width="100%",
            align="center",
            margin="0em",
            padding="0em",
            padding_top="0.3em",
            padding_bottom="1em",
            **props,
        )


header = Header.create
