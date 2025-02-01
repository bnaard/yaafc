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


def sidebar() -> rx.Component:
    return rx.flex(
        rx.vstack(
            sidebar_item_icon("files", href="/projects"),
        ),
        rx.spacer(),
        sidebar_profile(),
        sidebar_footer(),
        flex_direction="column",
        height="90vh",
        border="solid",
        border_color=rx.color("accent", 8),
        border_right="none",
        border_width="1px",
        padding="0.3em",
        margin="0em",
    )
