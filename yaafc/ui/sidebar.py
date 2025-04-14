import reflex as rx

import yaafc.ui as yui
from yaafc.config import menus
from yaafc.config.types import SidebarSection


class SidebarLink(rx.Component):
    @classmethod
    def create(cls, *children, href: str = "/", **props) -> rx.Component:
        return rx.link(*children, href=href, **props)


sidebar_link = SidebarLink.create


class SidebarIcon(rx.Component):
    @classmethod
    def create(
        cls, icon: str = "image", color: str = yui.Colors.ACCENT, href: str = "/", *children, **props
    ) -> rx.Component:
        props.setdefault("size", 26)
        props.setdefault("color", yui.color(color, 10))
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


class Section(rx.Component):
    @classmethod
    def create(cls, section: SidebarSection, *children, **props) -> rx.Component:
        return icon_stack(
            [sidebar_icon(icon=item.heroicon_icon_name, href=item.href) for item in section.items], *children, **props
        )


section = Section.create


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
            section(section=menus.sidebar["Tools"]),
            rx.spacer(),
            section(section=menus.sidebar["Profile"]),
            section(section=menus.sidebar["Footer"]),
            **props,
        )


sidebar = Sidebar.create
