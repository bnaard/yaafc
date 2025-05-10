import reflex as rx

import yaafc.ui as yui
from yaafc.templates.template import template


def show_layout(*components, **props) -> rx.Component:
    return rx.grid(
        *components,
        # rx.foreach(rx.Var.range(16), lambda i: yui.card_component()),
        yui.card_component(row_span=1, col_span=1),
        yui.card_component(row_span=1, col_span=1),
        yui.card_component(row_span=1, col_span=1),
        yui.card_component(row_span=1, col_span=1),
        yui.card_component(row_span=1, col_span=1),
        yui.card_component(row_span=1, col_span=1),
        yui.card_component(row_span=1, col_span=1),
        yui.card_component(row_span=1, col_span=1),
        yui.card_component(row_span=1, col_span=1),
        gap="1rem",
        grid_template_columns=[
            "1fr",  # 1 column for mobile
            "repeat(2, 1fr)",  # 2 columns for tablet
            "repeat(2, 1fr)",  # 2 columns for small desktop
            "repeat(4, 1fr)",  # 3 columns for medium desktop
            "repeat(4, 1fr)",  # 4 columns for large desktop
        ],
        grid_template_rows=[
            "1fr",  # 1 column for mobile
            "repeat(2, 1fr)",  # 2 columns for tablet
            "repeat(3, 1fr)",  # 2 columns for small desktop
            "repeat(4, 1fr)",  # 3 columns for medium desktop
            "repeat(4, 1fr)",  # 4 columns for large desktop
        ],
        justify="center",
        **props,
    )


@template(template="main", route="/layout", title="YAAFC")
def layout() -> rx.Component:
    return rx.flex(
        rx.card(width="15vw", background_color=rx.color("accent", 2)),
        show_layout(spacing="4", width="100%", height="100%"),
        direction="row",
        spacing="4",
    )


# rx.vstack(
#     rx.card(
#         "Card",
#         width="100%",
#         height="260px",
#     ),
#     grid_column="span 2",  # This makes the card span 2 columns
# )
