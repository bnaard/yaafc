from typing import Callable, Literal

import reflex as rx

from yaafc.config.constants import Colors
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
        all_meta = [*default_meta, *(meta or [])]

        templated_page = main_template(page_content) if template == "main" else main_template(page_content)

        @rx.page(
            route=route,
            title=title,
            description=description,
            meta=all_meta,
            script_tags=script_tags,
            on_load=on_load,
        )
        def theme_wrap():
            return rx.theme(
                templated_page,
                has_background=True,
                accent_color=Settings.theme["colors"][Colors.ACCENT]["name"],
                gray_color=Settings.theme["colors"][Colors.GRAY]["name"],
                radius=Settings.theme["styles"]["radius"],
                scaling=Settings.theme["styles"]["scaling"],
                panel_background=Settings.theme["styles"]["panel_background"],
            )

        return theme_wrap

    return decorator
