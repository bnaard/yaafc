import dataclasses

import reflex as rx


# ClipboardEvent: https://developer.mozilla.org/en-US/docs/Web/API/ClipboardEvent
@dataclasses.dataclass
class ClipboardEvent:
    """Represents events that provide access to the clipboard data."""

    clipboardData: str = ""  # The data on the clipboard (serialized as string)


def clipboard_event_spec(ev: rx.Var[ClipboardEvent]) -> tuple[rx.Var[ClipboardEvent]]:
    return (rx.Var.create(ClipboardEvent(clipboardData=ev.clipboardData)),)


@dataclasses.dataclass
class CopyEvent(ClipboardEvent):
    """Represents a copy event."""

    pass


def copy_event_spec(ev: rx.Var[CopyEvent]) -> tuple[rx.Var[CopyEvent]]:
    return (rx.Var.create(CopyEvent(**dataclasses.asdict(clipboard_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class CutEvent(ClipboardEvent):
    """Represents a cut event."""

    pass


def cut_event_spec(ev: rx.Var[CutEvent]) -> tuple[rx.Var[CutEvent]]:
    return (rx.Var.create(CutEvent(**dataclasses.asdict(clipboard_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class PasteEvent(ClipboardEvent):
    """Represents a paste event."""

    pass


def paste_event_spec(ev: rx.Var[PasteEvent]) -> tuple[rx.Var[PasteEvent]]:
    return (rx.Var.create(PasteEvent(**dataclasses.asdict(clipboard_event_spec(ev)[0].get()))),)
