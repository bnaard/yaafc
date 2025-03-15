"""Sidebar component for the app."""

import reflex as rx


def sidebar_item_icon(icon: str, color: str = "accent", href: str = "") -> rx.Component:
    return rx.link(
        rx.icon(icon, size=26, color=rx.color(color, 10), margin="0.4em"),
        href=href,
    )


def sidebar_profile() -> rx.Component:
    return rx.vstack(sidebar_item_icon("circle-user-round", href="/profile"), padding="0em", margin="0em")


def sidebar_footer() -> rx.Component:
    return rx.vstack(
        sidebar_item_icon("palette", href="/theming"),
        sidebar_item_icon("settings", href="/settings"),
        padding="0em",
        margin="0em",
    )


def show_logo(dark: bool = False) -> rx.Component:
    return rx.image(
        src="/logo.svg" if not dark else "/logo.svg",
        height="2em",
        justify="center",
        text_align="center",
        padding_x="0em",
        padding_top="0.2em",
        padding_bottom="0em",
        margin_bottom="0em",
    )


def sidebar() -> rx.Component:
    return rx.flex(
        rx.color_mode_cond(
            show_logo(),
            show_logo(dark=True),
        ),
        rx.box(height="2em"),
        rx.vstack(
            sidebar_item_icon("files", href="/projects"),
            sidebar_item_icon("files", href="/files"),
            spacing="1",
        ),
        rx.spacer(),
        sidebar_profile(),
        sidebar_footer(),
        flex_direction="column",
        height="100%",
        padding="0.3em",
        margin="0em",
        spacing="0",
        style={"position": "sticky", "top": "0"},
    )
