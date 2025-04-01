# """Styles for the app."""

import dataclasses

from yaafc.config.constants import Colors


@dataclasses.dataclass
class ThemeColorType:
    name: str
    strength: int


@dataclasses.dataclass
class ThemeStyleType:
    radius: str
    scaling: str
    panel_background: str
    has_background: bool


@dataclasses.dataclass
class ThemeType:
    colors: dict[str, ThemeColorType]
    styles: ThemeStyleType


themes = {
    "greener": ThemeType(
        colors={
            Colors.ACCENT: ThemeColorType(name="teal", strength=11),
            Colors.GRAY: ThemeColorType(name="olive", strength=11),
            Colors.BACKGROUND: ThemeColorType(name="olive", strength=12),
            Colors.WHITE: ThemeColorType(name="teal", strength=12),
            Colors.BLACK: ThemeColorType(name="teal", strength=1),
            Colors.INFO: ThemeColorType(name="indigo", strength=10),
            Colors.INFO_CONTENT: ThemeColorType(name="indigo", strength=2),
            Colors.SUCCESS: ThemeColorType(name="grass", strength=11),
            Colors.SUCCESS_CONTENT: ThemeColorType(name="grass", strength=2),
            Colors.WARNING: ThemeColorType(name="yellow", strength=10),
            Colors.WARNING_CONTENT: ThemeColorType(name="yellow", strength=2),
            Colors.ERROR: ThemeColorType(name="red", strength=11),
            Colors.ERROR_CONTENT: ThemeColorType(name="red", strength=2),
        },
        styles=ThemeStyleType(radius="none", scaling="100%", panel_background="solid", has_background=True),
    )
}
