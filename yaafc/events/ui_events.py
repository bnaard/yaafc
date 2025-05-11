"""
UI event dataclasses and event spec functions for DOM event handling.

This module provides Python representations of UI-related DOM events, including their event spec functions for use with Reflex event handlers.
"""

import dataclasses

import reflex as rx


@dataclasses.dataclass
class UIEvent:
    """
    Represents simple user interface events.

    Attributes:
        detail (int): Event-specific information (e.g., click count)
        view (str): The window object (serialized as string)
    """

    detail: int = 0  # Event-specific information (e.g., click count)
    view: str = ""  # The window object (serialized as string)


def ui_event_spec(ev: rx.Var[UIEvent]) -> tuple[rx.Var[UIEvent]]:
    """
    Event spec function for UIEvent.

    Args:
        ev (rx.Var[UIEvent]): The UIEvent variable.

    Returns:
        tuple[rx.Var[UIEvent]]: A tuple containing the processed UIEvent variable.
    """
    return (rx.Var.create(UIEvent(detail=ev.detail, view=ev.view)),)


@dataclasses.dataclass
class ScrollEvent(UIEvent):
    """
    Represents a scroll event.

    Inherits all attributes from UIEvent.
    """

    pass


def scroll_event_spec(ev: rx.Var[ScrollEvent]) -> tuple[rx.Var[ScrollEvent]]:
    """
    Event spec function for ScrollEvent.

    Args:
        ev (rx.Var[ScrollEvent]): The ScrollEvent variable.

    Returns:
        tuple[rx.Var[ScrollEvent]]: A tuple containing the processed ScrollEvent variable.
    """
    return (rx.Var.create(ScrollEvent(**dataclasses.asdict(ui_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class ScrollEndEvent(UIEvent):
    """
    Represents a scrollend event.

    Inherits all attributes from UIEvent.
    """

    pass


def scroll_end_event_spec(ev: rx.Var[ScrollEndEvent]) -> tuple[rx.Var[ScrollEndEvent]]:
    """
    Event spec function for ScrollEndEvent.

    Args:
        ev (rx.Var[ScrollEndEvent]): The ScrollEndEvent variable.

    Returns:
        tuple[rx.Var[ScrollEndEvent]]: A tuple containing the processed ScrollEndEvent variable.
    """
    return (rx.Var.create(ScrollEndEvent(**dataclasses.asdict(ui_event_spec(ev)[0].get()))),)
