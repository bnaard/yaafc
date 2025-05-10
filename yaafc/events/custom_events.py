import dataclasses

import reflex as rx


# CustomEvent: https://developer.mozilla.org/en-US/docs/Web/API/CustomEvent
@dataclasses.dataclass
class CustomEvent:
    """Represents events initialized by an application for any purpose."""

    detail: str = ""  # Any custom data passed with the event (serialized as string)


def custom_event_spec(ev: rx.Var[CustomEvent]) -> tuple[rx.Var[CustomEvent]]:
    return (rx.Var.create(CustomEvent(detail=ev.detail)),)
