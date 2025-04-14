import dataclasses


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


@dataclasses.dataclass
class SidebarMenuItem:
    heroicon_icon_name: str
    label: str
    href: str


@dataclasses.dataclass
class SidebarSection:
    name: str
    items: list[SidebarMenuItem]


@dataclasses.dataclass
class HeaderMenuItem:
    heroicon_icon_name: str
    label: str
    href: str
