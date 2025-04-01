# """Sidebar component for the app."""

# import reflex as rx


# def show_sidebar_item_icon(icon: str, color: str = "accent", href: str = "") -> rx.Component:
#     return rx.link(
#         rx.icon(icon, size=26, color=rx.color(color, 10), margin="0.4em"),
#         href=href,
#     )


# def show_profile() -> rx.Component:
#     return rx.vstack(show_sidebar_item_icon("circle-user-round", href="/profile"), padding="0em", margin="0em")


# def show_footer() -> rx.Component:
#     return rx.vstack(
#         show_sidebar_item_icon("grid-3x3", href="/grid"),
#         show_sidebar_item_icon("settings", href="/settings"),
#         padding="0em",
#         margin="0em",
#     )


# def show_logo() -> rx.Component:
#     def show_logo_light_dark(dark: bool = False) -> rx.Component:
#         return rx.link(
#             rx.image(
#                 src="/logo.svg" if not dark else "/logo.svg",
#                 width="100%",
#                 height="100%",
#                 fit="contain",
#             ),
#             height="2em",
#             width="100%",
#             justify="center",
#             text_align="center",
#             padding_x="0em",
#             padding_top="0.2em",
#             padding_bottom="0em",
#             margin_bottom="0em",
#             href="/",
#         )

#     return (
#         rx.color_mode_cond(
#             show_logo_light_dark(),
#             show_logo_light_dark(dark=True),
#         ),
#     )


# def show_tools() -> rx.Component:
#     return rx.vstack(
#         show_sidebar_item_icon("bookmark", href="/projects"),
#         show_sidebar_item_icon("folder-open-dot", href="/files"),
#         padding="0em",
#         margin="0em",
#         spacing="1",
#     )


# def sidebar() -> rx.Component:
#     return rx.flex(
#         show_logo(),
#         rx.box(height="2em"),
#         show_tools(),
#         rx.spacer(),
#         show_profile(),
#         show_footer(),
#         flex_direction="column",
#         height="100%",
#         padding="0.3em",
#         margin="0em",
#         spacing="0",
#         style={"position": "sticky", "top": "0"},
#     )
