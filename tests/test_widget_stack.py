import pytest
import reflex as rx

from yaafc.ui.widgets.widget_stack import WidgetStack


def widget_a():
    return rx.text("WidgetA")


def widget_b():
    return rx.text("WidgetB")


def test_register_and_render_widgets():
    WidgetStack.widgets.clear()
    WidgetStack.registerWidget("A", widget_a)
    WidgetStack.registerWidget("B", widget_b)
    comp = WidgetStack.get_component()
    assert isinstance(comp, rx.Component)
    # Should render both widgets
    children = comp.children[0].children if hasattr(comp, "children") and comp.children else []
    assert any(getattr(child, "text", None) == "WidgetA" for child in children)
    assert any(getattr(child, "text", None) == "WidgetB" for child in children)


def test_registerWidget_overwrite():
    WidgetStack.widgets.clear()
    WidgetStack.registerWidget("A", widget_a)
    WidgetStack.registerWidget("A", widget_b)
    assert WidgetStack.widgets["A"] is widget_b


def test_registerWidget_invalid():
    WidgetStack.widgets.clear()
    with pytest.raises(TypeError):
        WidgetStack.registerWidget("A", None)
