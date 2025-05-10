import dataclasses

import reflex as rx


# UIEvent: https://developer.mozilla.org/en-US/docs/Web/API/UIEvent
@dataclasses.dataclass
class UIEvent:
    """Represents simple user interface events."""

    detail: int = 0  # Event-specific information (e.g., click count)
    view: str = ""  # The window object (serialized as string)


def ui_event_spec(ev: rx.Var[UIEvent]) -> tuple[rx.Var[UIEvent]]:
    return (rx.Var.create(UIEvent(detail=ev.detail, view=ev.view)),)


@dataclasses.dataclass
class ScrollEvent(UIEvent):
    """Represents a scroll event."""

    pass


def scroll_event_spec(ev: rx.Var[ScrollEvent]) -> tuple[rx.Var[ScrollEvent]]:
    return (rx.Var.create(ScrollEvent(**dataclasses.asdict(ui_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class ScrollEndEvent(UIEvent):
    """Represents a scrollend event."""

    pass


def scroll_end_event_spec(ev: rx.Var[ScrollEndEvent]) -> tuple[rx.Var[ScrollEndEvent]]:
    return (rx.Var.create(ScrollEndEvent(**dataclasses.asdict(ui_event_spec(ev)[0].get()))),)
