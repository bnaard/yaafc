import reflex as rx

import yaafc.config.styles as styles


class Settings(rx.State):
    theme_name: str = "greener"
    theme: styles.ThemeType = styles.themes[theme_name]
