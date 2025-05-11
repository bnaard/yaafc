"""
Custom event dataclass and event spec function for DOM event handling.

This module provides a Python representation of CustomEvent for use with Reflex event handlers.
"""

import dataclasses

import reflex as rx


@dataclasses.dataclass
class CustomEvent:
    """
    Represents events initialized by an application for any purpose.

    Attributes:
        detail (str): Any custom data passed with the event (serialized as string)
    """

    detail: str = ""  # Any custom data passed with the event (serialized as string)


def custom_event_spec(ev: rx.Var[CustomEvent]) -> tuple[rx.Var[CustomEvent]]:
    """
    Specifies the structure of a custom event for Reflex event handling.

    Args:
        ev (rx.Var[CustomEvent]): The custom event variable.

    Returns:
        tuple[rx.Var[CustomEvent]]: A tuple containing the custom event variable.
    """
    return (rx.Var.create(CustomEvent(detail=ev.detail)),)
