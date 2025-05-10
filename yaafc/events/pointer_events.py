import dataclasses

import reflex as rx


# PointerEvent: https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent
@dataclasses.dataclass
class PointerEvent:
    """Represents events that occur when a pointer (mouse, pen, touch, etc.) interacts with the surface."""

    pointerId: int = 0  # Unique ID for the pointer
    width: float = 1.0  # Width of the pointer's contact geometry
    height: float = 1.0  # Height of the pointer's contact geometry
    pressure: float = 0.0  # Pressure of the pointer
    tangentialPressure: float = 0.0  # Tangential pressure
    tiltX: int = 0  # Tilt of the pointer in X
    tiltY: int = 0  # Tilt of the pointer in Y
    twist: int = 0  # Rotation of the pointer
    pointerType: str = "mouse"  # Type of pointer (mouse, pen, touch)
    isPrimary: bool = True  # True if primary pointer
    # MouseEvent properties (for completeness, can be inherited in practice)
    altKey: bool = False
    button: int = 0
    buttons: int = 0
    clientX: int = 0
    clientY: int = 0
    ctrlKey: bool = False
    metaKey: bool = False
    movementX: int = 0
    movementY: int = 0
    offsetX: int = 0
    offsetY: int = 0
    pageX: int = 0
    pageY: int = 0
    relatedTarget: str = ""
    screenX: int = 0
    screenY: int = 0
    shiftKey: bool = False
    detail: int = 1


def pointer_event_spec(ev: rx.Var[PointerEvent]) -> tuple[rx.Var[PointerEvent]]:
    return (
        rx.Var.create(
            PointerEvent(
                pointerId=ev.pointerId,
                width=ev.width,
                height=ev.height,
                pressure=ev.pressure,
                tangentialPressure=ev.tangentialPressure,
                tiltX=ev.tiltX,
                tiltY=ev.tiltY,
                twist=ev.twist,
                pointerType=ev.pointerType,
                isPrimary=ev.isPrimary,
                altKey=ev.altKey,
                button=ev.button,
                buttons=ev.buttons,
                clientX=ev.clientX,
                clientY=ev.clientY,
                ctrlKey=ev.ctrlKey,
                metaKey=ev.metaKey,
                movementX=ev.movementX,
                movementY=ev.movementY,
                offsetX=ev.offsetX,
                offsetY=ev.offsetY,
                pageX=ev.pageX,
                pageY=ev.pageY,
                relatedTarget=ev.relatedTarget,
                screenX=ev.screenX,
                screenY=ev.screenY,
                shiftKey=ev.shiftKey,
                detail=ev.detail,
            )
        ),
    )


@dataclasses.dataclass
class GotPointerCaptureEvent(PointerEvent):
    """Represents a gotpointercapture event."""

    pass


def got_pointer_capture_event_spec(ev: rx.Var[GotPointerCaptureEvent]) -> tuple[rx.Var[GotPointerCaptureEvent]]:
    return (rx.Var.create(GotPointerCaptureEvent(**dataclasses.asdict(pointer_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class LostPointerCaptureEvent(PointerEvent):
    """Represents a lostpointercapture event."""

    pass


def lost_pointer_capture_event_spec(ev: rx.Var[LostPointerCaptureEvent]) -> tuple[rx.Var[LostPointerCaptureEvent]]:
    return (rx.Var.create(LostPointerCaptureEvent(**dataclasses.asdict(pointer_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class PointerCancelEvent(PointerEvent):
    """Represents a pointercancel event."""

    pass


def pointer_cancel_event_spec(ev: rx.Var[PointerCancelEvent]) -> tuple[rx.Var[PointerCancelEvent]]:
    return (rx.Var.create(PointerCancelEvent(**dataclasses.asdict(pointer_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class PointerDownEvent(PointerEvent):
    """Represents a pointerdown event."""

    pass


def pointer_down_event_spec(ev: rx.Var[PointerDownEvent]) -> tuple[rx.Var[PointerDownEvent]]:
    return (rx.Var.create(PointerDownEvent(**dataclasses.asdict(pointer_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class PointerEnterEvent(PointerEvent):
    """Represents a pointerenter event."""

    pass


def pointer_enter_event_spec(ev: rx.Var[PointerEnterEvent]) -> tuple[rx.Var[PointerEnterEvent]]:
    return (rx.Var.create(PointerEnterEvent(**dataclasses.asdict(pointer_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class PointerLeaveEvent(PointerEvent):
    """Represents a pointerleave event."""

    pass


def pointer_leave_event_spec(ev: rx.Var[PointerLeaveEvent]) -> tuple[rx.Var[PointerLeaveEvent]]:
    return (rx.Var.create(PointerLeaveEvent(**dataclasses.asdict(pointer_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class PointerMoveEvent(PointerEvent):
    """Represents a pointermove event."""

    pass


def pointer_move_event_spec(ev: rx.Var[PointerMoveEvent]) -> tuple[rx.Var[PointerMoveEvent]]:
    return (rx.Var.create(PointerMoveEvent(**dataclasses.asdict(pointer_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class PointerOutEvent(PointerEvent):
    """Represents a pointerout event."""

    pass


def pointer_out_event_spec(ev: rx.Var[PointerOutEvent]) -> tuple[rx.Var[PointerOutEvent]]:
    return (rx.Var.create(PointerOutEvent(**dataclasses.asdict(pointer_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class PointerOverEvent(PointerEvent):
    """Represents a pointerover event."""

    pass


def pointer_over_event_spec(ev: rx.Var[PointerOverEvent]) -> tuple[rx.Var[PointerOverEvent]]:
    return (rx.Var.create(PointerOverEvent(**dataclasses.asdict(pointer_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class PointerUpEvent(PointerEvent):
    """Represents a pointerup event."""

    pass


def pointer_up_event_spec(ev: rx.Var[PointerUpEvent]) -> tuple[rx.Var[PointerUpEvent]]:
    return (rx.Var.create(PointerUpEvent(**dataclasses.asdict(pointer_event_spec(ev)[0].get()))),)
