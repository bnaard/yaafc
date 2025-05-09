# from dataclasses import dataclass
# from typing import Optional, TypeAlias

import reflex as rx

import yaafc.config.styles as styles

# @dataclass
# class Slot:
#     row: int
#     col: int
#     rowspan: int = 1
#     colspan: int = 1
#     slot_id: Optional[int] = None

# Slots: TypeAlias = list[Slot]


class Settings(rx.State):
    selected_theme_name: str = "greener"
    theme: styles.ThemeType = styles.themes[selected_theme_name]
