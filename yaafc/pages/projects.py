import reflex as rx

import yaafc.ui as yui
from yaafc.templates.template import template

# project_page_settings = {
#     "template": "main",
#     "route": "/projects",
#     "title": "Projects",
#     "description": "Projects page",
#     "slots": [
#         Slot(1, 1, 1, 1, 1),
#         Slot(1, 2, 1, 1, 2),
#         Slot(1, 3, 1, 1, 3),
#         Slot(1, 4, 1, 1, 4),
#         Slot(2, 1, 1, 1, 5),
#         Slot(2, 2, 1, 1, 6),
#         Slot(2, 3, 1, 1, 7),
#         Slot(2, 4, 1, 1, 8),
#         Slot(3, 1, 1, 1, 9),
#         Slot(3, 2, 1, 1, 10),
#         Slot(3, 3, 1, 1, 11),
#         Slot(3, 4, 1, 1, 12),
#         Slot(4, 1, 1, 1, 13),
#         Slot(4, 2, 1, 1, 14),
#         Slot(4, 3, 1, 1, 15),
#         Slot(4, 4, 1, 1, 16),
#     ],
#     "active_slot": 2,
# }


# class ProjectPage(rx.State):
#     """State for the project page."""

#     _template: str | None = project_page_settings["template"]
#     _page_route: str | None = project_page_settings["route"]
#     _title: str | None = project_page_settings["title"]
#     _description: str | None = project_page_settings["description"]
#     page_id: str | None = "projects"
#     _slots: list[Slot] | None = project_page_settings["slots"]
#     # active_slot: int = project_page_settings["active_slot"]
#     _meta: str | None = None
#     _script_tags: list[rx.Component] | None = None
#     _on_load: rx.EventHandler | list[rx.EventHandler] | None = None


@template(
    route="/projects",
    title="Projects",
    description="Projects page",
)
def projects() -> rx.Component:
    return rx.box(
        yui.table(page_id=rx.State.router.page.path, slot_id=1),
        background_color=rx.Color("accent", 2),
        justify="center",
        padding="0em",
        margin="0em",
        height="100%",
    )
