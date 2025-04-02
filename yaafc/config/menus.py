from yaafc.config.types import SideBarMenuItem, SideBarSection

sidebar = {
    "Tools": SideBarSection(
        name="Tools",
        items=[
            SideBarMenuItem(
                heroicon_icon_name="bookmark",
                href="/projects",
            ),
            SideBarMenuItem(
                heroicon_icon_name="folder-open-dot",
                href="/files",
            ),
        ],
    ),
    "Profile": SideBarSection(
        name="Profile",
        items=[
            SideBarMenuItem(
                heroicon_icon_name="circle-user-round",
                href="/profile",
            ),
        ],
    ),
    "Footer": SideBarSection(
        name="Footer",
        items=[
            SideBarMenuItem(
                heroicon_icon_name="grid-3x3",
                href="/grid",
            ),
            SideBarMenuItem(
                heroicon_icon_name="settings",
                href="/settings",
            ),
        ],
    ),
}
