from collections.abc import Callable

import reflex as rx

from yaafc.config import styles


def default_template(page_content: Callable[[], rx.Component]) -> rx.Component:
    return rx.flex(
        page_content(),
        flex_direction=[
            "column",
            "column",
            "column",
            "column",
            "column",
            "row",
        ],
        max_width=[
            "100%",
            "100%",
            "100%",
            "100%",
            "100%",
            styles.max_width,
        ],
        **styles.template_content_style,
    )

    # return rx.flex(
    #     rx.vstack(
    #         navbar(),
    #         # sidebar(),
    #         rx.flex(
    #             rx.vstack(
    #                 page_content(),
    #                 width="100%",
    #                 **styles.template_content_style,
    #             ),
    #             width="100%",
    #             **styles.template_page_style,
    #             max_width=[
    #                 "100%",
    #                 "100%",
    #                 "100%",
    #                 "100%",
    #                 "100%",
    #                 styles.max_width,
    #             ],
    #         ),
    #     ),
    #     flex_direction=[
    #         "column",
    #         "column",
    #         "column",
    #         "column",
    #         "column",
    #         "row",
    #     ],
    #     width="100%",
    #     margin="auto",
    #     position="relative",
    # )
