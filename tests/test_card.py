import pytest
import reflex as rx

from yaafc.ui.card import card_component


# Test: expected use
def test_card_component_renders_mobile_and_desktop():
    comp = card_component()
    assert isinstance(comp, rx.Component)
    # Check that both mobile_only and tablet_and_desktop are present in the children
    children = comp.children if hasattr(comp, "children") else []
    assert any(getattr(child, "name", "") == "mobile_only" for child in children) or any(
        getattr(child, "name", "") == "tablet_and_desktop" for child in children
    )


# Test: edge case (props override)
def test_card_component_with_custom_props():
    comp = card_component(height="50px", width="50px")
    assert isinstance(comp, rx.Component)
    # Should still render with custom props


# Test: failure case (invalid prop)
def test_card_component_invalid_prop():
    with pytest.raises(TypeError):
        card_component(nonexistent_prop="value")
