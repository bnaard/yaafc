from typing import Callable, Literal

import reflex as rx

import yaafc.ui as yui
from yaafc.config.meta import default_meta
from yaafc.states.settings import Settings
from yaafc.templates.main import main_template


def template(
    template: Literal["main"] | None = "main",
    route: str | None = None,
    title: str | None = None,
    description: str | None = None,
    meta: str | None = None,
    script_tags: list[rx.Component] | None = None,
    on_load: rx.EventHandler | list[rx.EventHandler] | None = None,
    active_slot: int | None = 1,
) -> Callable[[Callable[[], rx.Component]], rx.Component]:
    """The template for each page of the app.

    Args:
        template: The kind of template to use.
        route: The route to reach the page.
        title: The title of the page.
        description: The description of the page.
        meta: Additionnal meta to add to the page.
        on_load: The event handler(s) called when the page load.
        script_tags: Scripts to attach to the page.

    Returns:
        The template with the page content.
    """

    def decorator(page_content: Callable[[], rx.Component]) -> rx.Component:
        """The template for each page of the app.

        Args:
            page_content: The content of the page.

        Returns:
            The template with the page content.
        """
        # Get the meta tags for the page.
        effective_meta = [*default_meta, *(meta or [])]

        def template_func() -> rx.Component:
            Settings.active_page_id = route
            Settings.active_slot = active_slot

            if template is None or template == "main" or template == "default":
                return main_template(page_content)
            else:
                return main_template(page_content)

        templated_page = template_func()

        @rx.page(
            route=route,
            title=title,
            description=description,
            meta=effective_meta,
            script_tags=script_tags,
            on_load=on_load,
        )
        def theme_wrap():
            return rx.theme(
                templated_page,
                has_background=True,
                accent_color=Settings.theme["colors"][yui.Colors.ACCENT]["name"],
                gray_color=Settings.theme["colors"][yui.Colors.GRAY]["name"],
                radius=Settings.theme["styles"]["radius"],
                scaling=Settings.theme["styles"]["scaling"],
                panel_background=Settings.theme["styles"]["panel_background"],
            )

        return theme_wrap

    return decorator
