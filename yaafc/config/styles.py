"""Styles for the app."""

import reflex as rx

theme_accent_color = "teal"
theme_gray_color = "olive"

border_radius = "var(--radius-2)"
border = f"1px solid {rx.color('gray', 5)}"
text_color = rx.color("gray", 11)
gray_color = rx.color("gray", 11)
gray_bg_color = rx.color("gray", 3)
accent_text_color = rx.color("accent", 10)
accent_color = rx.color("accent", 1)
accent_bg_color = rx.color("accent", 3)
hover_accent_color = {"_hover": {"color": accent_text_color}}
hover_accent_bg = {"_hover": {"background_color": accent_color}}
content_width_vw = "90vw"
sidebar_width = "32em"
sidebar_content_width = "16em"
max_width = "100%"
color_box_size = ["2.25rem", "2.25rem", "2.5rem"]

template_page_style = {
    "padding_top": ["1em", "1em", "2em"],
    "padding_x": ["auto", "auto", "2em"],
}

template_content_style = {
    "padding": "1em",
    "margin_bottom": "2em",
    "min_height": "90vh",
}


# <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%22256%22 height=%22256%22 viewBox=%220 0 100 100%22><rect width=%22100%22 height=%22100%22 rx=%2220%22 fill=%22%23008573%22></rect><path d=%22M44.44 85.80Q43.04 88.59 40.73 88.59Q38.43 88.59 38.43 86.23L38.43 86.23Q38.43 84.78 39.82 83.06L39.82 83.06Q42.61 79.73 45.14 75.38L45.14 75.38L47.88 70.49L15.97 12.00L47.29 12.00L62.65 44.39L76.40 19.95Q77.90 17.16 78.98 14.28Q80.05 11.41 81.82 11.41L81.82 11.41Q84.03 11.41 84.03 13.61L84.03 13.61Q84.03 14.90 83.06 16.56L83.06 16.56L46.32 82.09Q45.73 83.17 45.35 83.86L45.35 83.86L44.44 85.80Z%22 fill=%22%23fff%22></path></svg>" />
#
# # https://formito.com/tools/favicon
