import reflex as rx

import yaafc.ui as yui
from yaafc.states.settings import Settings
from yaafc.templates.template import template


@template(template="main", route="/projects", title="YAAFC")
def projects() -> rx.Component:
    projects_table = yui.table()
    Settings.active_widget = projects_table.widget_id

    return rx.box(
        projects_table,
        background_color=rx.Color("accent", 2),
        justify="center",
        padding="0em",
        margin="0em",
        height="100%",
    )
