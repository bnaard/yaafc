"""
Clipboard event dataclasses and event spec functions for DOM event handling.

This module provides Python representations of clipboard-related DOM events, including their event spec functions for use with Reflex event handlers.
"""

import dataclasses

import reflex as rx


@dataclasses.dataclass
class ClipboardEvent:
    """
    Represents events that provide access to the clipboard data.

    Attributes:
        clipboardData (str): The data on the clipboard (serialized as string)
    """

    clipboardData: str = ""  # The data on the clipboard (serialized as string)


def clipboard_event_spec(ev: rx.Var[ClipboardEvent]) -> tuple[rx.Var[ClipboardEvent]]:
    """
    Creates a specification for a ClipboardEvent.

    Args:
        ev (rx.Var[ClipboardEvent]): The ClipboardEvent variable.

    Returns:
        tuple[rx.Var[ClipboardEvent]]: A tuple containing the ClipboardEvent variable.
    """
    return (rx.Var.create(ClipboardEvent(clipboardData=ev.clipboardData)),)


@dataclasses.dataclass
class CopyEvent(ClipboardEvent):
    """
    Represents a copy event.

    Inherits all attributes from ClipboardEvent.
    """

    pass


def copy_event_spec(ev: rx.Var[CopyEvent]) -> tuple[rx.Var[CopyEvent]]:
    """
    Creates a specification for a CopyEvent.

    Args:
        ev (rx.Var[CopyEvent]): The CopyEvent variable.

    Returns:
        tuple[rx.Var[CopyEvent]]: A tuple containing the CopyEvent variable.
    """
    return (rx.Var.create(CopyEvent(**dataclasses.asdict(clipboard_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class CutEvent(ClipboardEvent):
    """
    Represents a cut event.

    Inherits all attributes from ClipboardEvent.
    """

    pass


def cut_event_spec(ev: rx.Var[CutEvent]) -> tuple[rx.Var[CutEvent]]:
    """
    Creates a specification for a CutEvent.

    Args:
        ev (rx.Var[CutEvent]): The CutEvent variable.

    Returns:
        tuple[rx.Var[CutEvent]]: A tuple containing the CutEvent variable.
    """
    return (rx.Var.create(CutEvent(**dataclasses.asdict(clipboard_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class PasteEvent(ClipboardEvent):
    """
    Represents a paste event.

    Inherits all attributes from ClipboardEvent.
    """

    pass


def paste_event_spec(ev: rx.Var[PasteEvent]) -> tuple[rx.Var[PasteEvent]]:
    """
    Creates a specification for a PasteEvent.

    Args:
        ev (rx.Var[PasteEvent]): The PasteEvent variable.

    Returns:
        tuple[rx.Var[PasteEvent]]: A tuple containing the PasteEvent variable.
    """
    return (rx.Var.create(PasteEvent(**dataclasses.asdict(clipboard_event_spec(ev)[0].get()))),)
