import dataclasses

import reflex as rx


# FocusEvent: https://developer.mozilla.org/en-US/docs/Web/API/FocusEvent
@dataclasses.dataclass
class FocusEvent:
    """Represents events that occur when an element has received or lost focus."""

    relatedTarget: str = ""  # The secondary target for the event (element losing/gaining focus)


def focus_event_spec(ev: rx.Var[FocusEvent]) -> tuple[rx.Var[FocusEvent]]:
    return (rx.Var.create(FocusEvent(relatedTarget=ev.relatedTarget)),)


@dataclasses.dataclass
class BlurEvent(FocusEvent):
    """Represents a blur event."""

    pass


def blur_event_spec(ev: rx.Var[BlurEvent]) -> tuple[rx.Var[BlurEvent]]:
    return (rx.Var.create(BlurEvent(**dataclasses.asdict(focus_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class FocusInEvent(FocusEvent):
    """Represents a focus event (focusin)."""

    pass


def focus_in_event_spec(ev: rx.Var[FocusInEvent]) -> tuple[rx.Var[FocusInEvent]]:
    return (rx.Var.create(FocusInEvent(**dataclasses.asdict(focus_event_spec(ev)[0].get()))),)
