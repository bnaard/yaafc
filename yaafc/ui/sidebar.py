import reflex as rx


class SidebarLink(rx.Component):
    @classmethod
    def create(cls, *children, href: str = "/", **props) -> rx.Component:
        return rx.link(*children, href=href, **props)


sidebar_link = SidebarLink.create


class SidebarIcon(rx.Component):
    @classmethod
    def create(cls, icon: str = "image", color: str = "accent", href: str = "/", *children, **props) -> rx.Component:
        props.setdefault("size", 26)
        props.setdefault("color", rx.color(color, 10))
        props.setdefault("margin", "0.4em")
        return sidebar_link(
            rx.flex(
                rx.icon(icon, **props),
                *children,
                direction="column",
            ),
            href=href,
        )


sidebar_icon = SidebarIcon.create


# def show_sidebar_item_icon(icon: str, color: str = "accent", href: str = "") -> rx.Component:
#     return rx.link(
#         rx.icon(icon, size=26, color=rx.color(color, 10), margin="0.4em"),
#         href=href,
#     )


class IconStack(rx.Component):
    @classmethod
    def create(cls, *children, **props) -> rx.Component:
        props.setdefault("padding", "0em")
        props.setdefault("margin", "0em")
        props.setdefault("spacing", "1")
        props.setdefault("direction", "column")
        props.setdefault("align", "center")
        return rx.flex(*children, **props)


icon_stack = IconStack.create


class Logo(rx.Component):
    @classmethod
    def create(cls, dark: bool = False, href: str = "/", **props) -> rx.Component:
        props.setdefault("height", "2em")
        props.setdefault("width", "100%")
        props.setdefault("justify", "center")
        props.setdefault("text_align", "center")
        props.setdefault("padding_x", "0em")
        props.setdefault("padding_top", "0.2em")
        props.setdefault("padding_bottom", "0em")
        props.setdefault("margin_bottom", "0em")
        return sidebar_link(
            rx.flex(
                rx.image(
                    src="/logo.svg" if not dark else "/logo.svg",
                    width="70%",
                    height="70%",
                    fit="contain",
                ),
                direction="column",
                align="center",
            ),
            href=href,
            **props,
        )


logo = Logo.create


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


class SectionLogo(rx.Component):
    @classmethod
    def create(cls, **props) -> rx.Component:
        return (
            rx.color_mode_cond(
                logo(**props),
                logo(dark=True, **props),
            ),
        )


section_logo = SectionLogo.create


class SectionTools(rx.Component):
    @classmethod
    def create(cls, *children, **props) -> rx.Component:
        return icon_stack(
            sidebar_icon("bookmark", href="/projects"),
            sidebar_icon("folder-open-dot", href="/files"),
        )


section_tools = SectionTools.create


# def show_tools() -> rx.Component:
#     return rx.vstack(
#         show_sidebar_item_icon("bookmark", href="/projects"),
#         show_sidebar_item_icon("folder-open-dot", href="/files"),
#         padding="0em",
#         margin="0em",
#         spacing="1",
#     )


class SectionProfile(rx.Component):
    @classmethod
    def create(cls, *children, **props) -> rx.Component:
        return icon_stack(
            sidebar_icon("circle-user-round", href="/profile"),
        )


section_profile = SectionProfile.create

# def show_profile() -> rx.Component:
#     return rx.vstack(show_sidebar_item_icon("circle-user-round", href="/profile"), padding="0em", margin="0em")


class SectionFooter(rx.Component):
    @classmethod
    def create(cls, *children, **props) -> rx.Component:
        return icon_stack(
            sidebar_icon("grid-3x3", href="/grid"),
            sidebar_icon("settings", href="/settings"),
        )


section_footer = SectionFooter.create


class Sidebar(rx.ComponentState):
    @classmethod
    def get_component(cls, **props) -> rx.Component:
        props.setdefault("height", "100%")
        props.setdefault("padding", "0.3em")
        props.setdefault("margin", "0em")
        props.setdefault("spacing", "0")
        props.setdefault("style", {"position": "sticky", "top": "0"})
        props.setdefault("direction", "column")

        return rx.flex(
            section_logo(),
            rx.box(height="1.2em"),
            section_tools(),
            rx.spacer(),
            section_profile(),
            section_footer(),
            **props,
        )


sidebar = Sidebar.create
