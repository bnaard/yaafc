"""
Touch event dataclass and event spec function for DOM event handling.

This module provides a Python representation of TouchEvent for use with Reflex event handlers.
"""

import dataclasses

import reflex as rx


@dataclasses.dataclass
class TouchEvent:
    """
    Represents events that occur when the user interacts with a touch screen.

    Attributes:
        altKey (bool): True if Alt key was pressed
        ctrlKey (bool): True if Ctrl key was pressed
        metaKey (bool): True if Meta (Cmd) key was pressed
        shiftKey (bool): True if Shift key was pressed
        touches (str): List of all current touches (serialized as string)
        targetTouches (str): List of touches on the target element (serialized as string)
        changedTouches (str): List of touches that changed (serialized as string)
    """

    altKey: bool = False  # True if Alt key was pressed
    ctrlKey: bool = False  # True if Ctrl key was pressed
    metaKey: bool = False  # True if Meta (Cmd) key was pressed
    shiftKey: bool = False  # True if Shift key was pressed
    touches: str = ""  # List of all current touches (serialized as string)
    targetTouches: str = ""  # List of touches on the target element (serialized as string)
    changedTouches: str = ""  # List of touches that changed (serialized as string)


def touch_event_spec(ev: rx.Var[TouchEvent]) -> tuple[rx.Var[TouchEvent]]:
    """
    Creates a tuple containing a Reflex variable for a TouchEvent.

    Args:
        ev (rx.Var[TouchEvent]): The TouchEvent variable to be processed.

    Returns:
        tuple[rx.Var[TouchEvent]]: A tuple containing the Reflex variable for the TouchEvent.
    """
    return (
        rx.Var.create(
            TouchEvent(
                altKey=ev.altKey,
                ctrlKey=ev.ctrlKey,
                metaKey=ev.metaKey,
                shiftKey=ev.shiftKey,
                touches=ev.touches,
                targetTouches=ev.targetTouches,
                changedTouches=ev.changedTouches,
            )
        ),
    )
