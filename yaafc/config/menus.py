from yaafc.config.types import HeaderMenuItem, SidebarMenuItem, SidebarSection

sidebar = {
    "Tools": SidebarSection(
        name="Tools",
        items=[
            SidebarMenuItem(
                heroicon_icon_name="bookmark",
                label="Projects",
                href="/projects",
            ),
            SidebarMenuItem(
                heroicon_icon_name="folder-open-dot",
                label="Files",
                href="/files",
            ),
        ],
    ),
    "Profile": SidebarSection(
        name="Profile",
        items=[
            SidebarMenuItem(
                heroicon_icon_name="circle-user-round",
                label="Profile",
                href="/profile",
            ),
        ],
    ),
    "Footer": SidebarSection(
        name="Footer",
        items=[
            SidebarMenuItem(
                heroicon_icon_name="grid-3x3",
                label="Layout",
                href="/layout",
            ),
            SidebarMenuItem(
                heroicon_icon_name="settings",
                label="Settings",
                href="/settings",
            ),
        ],
    ),
}


header = [
    HeaderMenuItem(
        heroicon_icon_name="grid-3x3",
        label="Docs",
        href="/docs",
    ),
]
