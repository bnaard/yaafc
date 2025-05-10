import dataclasses

import reflex as rx


# TouchEvent: https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent
@dataclasses.dataclass
class TouchEvent:
    """Represents events that occur when the user interacts with a touch screen."""

    altKey: bool = False  # True if Alt key was pressed
    ctrlKey: bool = False  # True if Ctrl key was pressed
    metaKey: bool = False  # True if Meta (Cmd) key was pressed
    shiftKey: bool = False  # True if Shift key was pressed
    touches: str = ""  # List of all current touches (serialized as string)
    targetTouches: str = ""  # List of touches on the target element (serialized as string)
    changedTouches: str = ""  # List of touches that changed (serialized as string)


def touch_event_spec(ev: rx.Var[TouchEvent]) -> tuple[rx.Var[TouchEvent]]:
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
