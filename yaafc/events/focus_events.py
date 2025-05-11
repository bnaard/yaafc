"""
Focus event dataclasses and event spec functions for DOM event handling.

This module provides Python representations of focus-related DOM events, including their event spec functions for use with Reflex event handlers.
"""

import dataclasses

import reflex as rx


# FocusEvent: https://developer.mozilla.org/en-US/docs/Web/API/FocusEvent
@dataclasses.dataclass
class FocusEvent:
    """
    Represents events that occur when an element has received or lost focus.

    Attributes:
        relatedTarget (str): The secondary target for the event (element losing/gaining focus)
    """

    relatedTarget: str = ""  # The secondary target for the event (element losing/gaining focus)


def focus_event_spec(ev: rx.Var[FocusEvent]) -> tuple[rx.Var[FocusEvent]]:
    """
    Event spec function for FocusEvent.

    Args:
        ev (rx.Var[FocusEvent]): The FocusEvent variable.

    Returns:
        tuple[rx.Var[FocusEvent]]: A tuple containing the FocusEvent variable.
    """
    return (rx.Var.create(FocusEvent(relatedTarget=ev.relatedTarget)),)


@dataclasses.dataclass
class BlurEvent(FocusEvent):
    """
    Represents a blur event.
    Inherits all attributes from FocusEvent.
    """

    pass


def blur_event_spec(ev: rx.Var[BlurEvent]) -> tuple[rx.Var[BlurEvent]]:
    """
    Event spec function for BlurEvent.

    Args:
        ev (rx.Var[BlurEvent]): The BlurEvent variable.

    Returns:
        tuple[rx.Var[BlurEvent]]: A tuple containing the BlurEvent variable.
    """
    return (rx.Var.create(BlurEvent(**dataclasses.asdict(focus_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class FocusInEvent(FocusEvent):
    """
    Represents a focus event (focusin).
    Inherits all attributes from FocusEvent.
    """

    pass


def focus_in_event_spec(ev: rx.Var[FocusInEvent]) -> tuple[rx.Var[FocusInEvent]]:
    """
    Event spec function for FocusInEvent.

    Args:
        ev (rx.Var[FocusInEvent]): The FocusInEvent variable.

    Returns:
        tuple[rx.Var[FocusInEvent]]: A tuple containing the FocusInEvent variable.
    """
    return (rx.Var.create(FocusInEvent(**dataclasses.asdict(focus_event_spec(ev)[0].get()))),)
