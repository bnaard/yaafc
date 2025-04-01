import reflex as rx

from yaafc.templates.template import template


def show_card() -> rx.Component:
    return rx.fragment(
        rx.mobile_only(
            rx.card(
                rx.vstack(
                    rx.icon("plus", color=rx.color("accent", 11), size=25),
                    align="center",
                    justify="center",
                    height="100%",
                ),
                height="100%",
                width="100%",
                style={
                    "_hover": {
                        "filter": "grayscale(50%) brightness(120%) opacity(80%)",
                    }
                },
            ),
        ),
        rx.tablet_and_desktop(
            rx.card(
                rx.vstack(
                    rx.icon("plus", color=rx.color("accent", 11), size=50),
                    align="center",
                    justify="center",
                    height="100%",
                ),
                height="100%",
                width="100%",
                style={
                    "_hover": {
                        "filter": "grayscale(50%) brightness(150%) opacity(80%)",
                    }
                },
            ),
        ),
    )


def show_grid(*components, **props) -> rx.Component:
    return rx.grid(
        *components,
        rx.foreach(rx.Var.range(16), lambda i: show_card()),
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


@template(template="main", route="/grid", title="YAAFC")
def grid() -> rx.Component:
    return rx.flex(
        rx.card(width="15vw", background_color=rx.color("accent", 2)),
        show_grid(spacing="4", width="100%", height="100%"),
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
