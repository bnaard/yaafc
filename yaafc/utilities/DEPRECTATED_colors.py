import yaafc.config.styles as styles
from yaafc.config.colors import radix_colors


def rgba_num(color: str, variation: int, dark: bool = False, alpha: bool = False) -> tuple[int, int, int, int]:
    if color is None:
        return (0, 0, 0, 1)
    if color == "accent":
        color = styles.theme_accent_color
    elif color == "gray":
        color = styles.theme_gray_color
    if color in radix_colors:
        return radix_colors[color]["dark" if dark else "light"]["alpha" if alpha else "regular"][variation - 1]
    else:
        return radix_colors["white"]["dark" if dark else "light"]["alpha" if alpha else "regular"][variation - 1]


def rgb_str(color: str, variation: int, dark: bool = False) -> str:
    return f"rgba{rgba_num(color, variation, dark, False)}"


def rgba_str(color: str, variation: int, dark: bool = False, alpha: bool = False) -> str:
    return f"rgba{rgba_num(color, variation, dark, alpha)}"


def rgb_hex(color: str, variation: int, dark: bool = False) -> str:
    return f"#{rgba_num(color, variation, dark, False)[0]:02x}{rgba_num(color, variation, dark, False)[1]:02x}{rgba_num(color, variation, dark, False)[2]:02x}"


def rgba_hex(color: str, variation: int, dark: bool = False, alpha: bool = False) -> str:
    return f"#{rgba_num(color, variation, dark, alpha)[0]:02x}{rgba_num(color, variation, dark, alpha)[1]:02x}{rgba_num(color, variation, dark, alpha)[2]:02x}{int(rgba_num(color, variation, dark, alpha)[3] * 255):02x}"
