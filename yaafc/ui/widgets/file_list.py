import reflex as rx

import yaafc.ui as yui


class FileList(rx.ComponentState):
    @classmethod
    def get_component(cls, **props) -> rx.Component:
        props.setdefault("height", "100%")
        props.setdefault("padding", "0.3em")
        props.setdefault("margin", "0em")
        props.setdefault("spacing", "0")
        props.setdefault("style", {"position": "sticky", "top": "0"})
        props.setdefault("direction", "column")

        return rx.flex(
            rx.box("Test", height="1.2em", backhround=yui.color(yui.WARNING)),
            **props,
        )


file_list = FileList.create
