import reflex as rx

import yaafc.config.styles as styles


class Settings(rx.State):
    selected_theme_name: str = "greener"
    theme: styles.ThemeType = styles.themes[selected_theme_name]
