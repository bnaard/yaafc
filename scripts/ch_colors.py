import fileinput
import re

_hex_colour = re.compile(r"#([0-9a-fA-F]{2}){1}([0-9a-fA-F]{2}){1}([0-9a-fA-F]{2}){1}([0-9a-fA-F]{2})?")


def replace(match):
    value = match.groups()
    rgb = (int(value[0], 16), int(value[1], 16), int(value[2], 16))
    alpha = 1
    if len(value) == 4:
        alpha = round(float(int(value[3], 16)) / 255.0, 2)
    return f"({rgb[0]!s}, {rgb[1]!s}, {rgb[2]!s}, {alpha!s})"


with fileinput.input(inplace=True, backup=".orig") as f:
    for line in f:
        line = _hex_colour.sub(replace, line)
        print(line, end="")
