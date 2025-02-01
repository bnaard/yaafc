import reflex as rx

from yaafc.components.file_list import file_list
from yaafc.templates.template import template


@template(template="main", route="/", title="YAAFC")
def index() -> rx.Component:
    return rx.vstack(
        file_list(),
        background_color=rx.Color("accent", 2),
        justify="center",
        height="90vh",
        padding="0em",
        margin="0em",
    )


# For each code block extract the color name and remove all enumerations in the color name. Then change the typescript code into a python data structure of form dict of list of str. The key of the dictionary is the extracted color name. The list shall be the enumerations attached to the color names of the original code.

# Change the typescript code into a python data structure. Change the inner dictionary into a list of strings. Then change the hexadecimal color definitions in the strings into tuples of 3 integers and 1 float value, where the last value is the float. Do the data change in place.

# Create regular expressions for search and replace in the marked code
