import reflex as rx

import yaafc.config.styles as styles


class ThemeState(rx.State):
    accent_color: str = styles.theme_accent_color
    gray_color: str = styles.theme_gray_color
    radius: str = "none"
    scaling: str = "100%"
    panel_background: str = "solid"
    has_background: bool = True
