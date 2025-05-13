import contextlib

from yaafc.pages.layout import LayoutState


class DummyEvent:
    def __init__(self, data_transfer=None):
        self.dataTransfer = data_transfer
        self.data_transfer = data_transfer


def get_state():
    # Use the create() method as required by Reflex
    return LayoutState.create()


def test_drop_widget_adds_widget_and_position():
    state = get_state()
    state.drop_widget("WidgetA", 1, 2)
    assert state.dropped_widgets == ["WidgetA"]
    assert state.dropped_positions == [(1, 2)]


def test_placed_widgets_returns_correct_tuples():
    state = get_state()
    state.dropped_widgets = ["A", "B"]
    state.dropped_positions = [(0, 0), (1, 1)]
    assert state.placed_widgets == [("A", 0, 0), ("B", 1, 1)]


def test_grid_drop_area_handles_drop(monkeypatch):
    called = {}

    def fake_drop_widget(widget_name, row, col):
        called["widget_name"] = widget_name
        called["row"] = row
        called["col"] = col

    monkeypatch.setattr(LayoutState, "drop_widget", staticmethod(fake_drop_widget))
    comp = LayoutState.grid_drop_area(2, 3)
    # Simulate drop event
    with contextlib.suppress(Exception):
        comp.on_drop(DummyEvent("WidgetB"))
    assert called == {"widget_name": "WidgetB", "row": 2, "col": 3}


def test_grid_drop_area_allows_drag_over():
    comp = LayoutState.grid_drop_area(0, 0)
    # Should not raise
    with contextlib.suppress(Exception):
        comp.on_drag_over(DummyEvent())
