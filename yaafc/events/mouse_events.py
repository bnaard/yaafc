import dataclasses

import reflex as rx
from reflex.vars.object import ObjectVar


# MouseEvent: https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent
@dataclasses.dataclass
class MouseEvent:
    """Represents events that occur due to the user interacting with a pointing device (mouse, pen, etc.)."""

    altKey: bool = False  # True if Alt key was pressed
    button: int = 0  # Which button was pressed (0=left, 1=middle, 2=right)
    buttons: int = 0  # Bitfield of buttons currently pressed
    clientX: int = 0  # X coordinate in viewport
    clientY: int = 0  # Y coordinate in viewport
    ctrlKey: bool = False  # True if Ctrl key was pressed
    metaKey: bool = False  # True if Meta (Cmd) key was pressed
    movementX: int = 0  # X movement since last event
    movementY: int = 0  # Y movement since last event
    offsetX: int = 0  # X relative to target element
    offsetY: int = 0  # Y relative to target element
    pageX: int = 0  # X relative to document
    pageY: int = 0  # Y relative to document
    relatedTarget: str = ""  # Secondary target (e.g., for mouseover/out)
    screenX: int = 0  # X relative to screen
    screenY: int = 0  # Y relative to screen
    shiftKey: bool = False  # True if Shift key was pressed
    detail: int = 1  # Number of consecutive clicks


def mouse_event_spec(ev: ObjectVar[MouseEvent]) -> tuple[rx.Var[MouseEvent]]:
    return (
        rx.Var.create(
            MouseEvent(
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


# WheelEvent: https://developer.mozilla.org/en-US/docs/Web/API/WheelEvent
@dataclasses.dataclass
class WheelEvent(MouseEvent):
    """Represents events that occur when the mouse wheel is rotated."""

    deltaX: float = 0.0  # Amount of horizontal scroll
    deltaY: float = 0.0  # Amount of vertical scroll
    deltaZ: float = 0.0  # Amount of z-axis scroll
    deltaMode: int = 0  # Unit of delta values (0=pixels, 1=lines, 2=pages)


def wheel_event_spec(ev: rx.Var[WheelEvent]) -> tuple[rx.Var[WheelEvent]]:
    return (
        rx.Var.create(
            WheelEvent(
                **dataclasses.asdict(mouse_event_spec(ev)[0].get()),
                deltaX=ev.deltaX,
                deltaY=ev.deltaY,
                deltaZ=ev.deltaZ,
                deltaMode=ev.deltaMode,
            )
        ),
    )


# PointerEvent: https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent
@dataclasses.dataclass
class PointerEvent(MouseEvent):
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


def pointer_event_spec(ev: rx.Var[PointerEvent]) -> tuple[rx.Var[PointerEvent]]:
    return (
        rx.Var.create(
            PointerEvent(
                **dataclasses.asdict(mouse_event_spec(ev)[0].get()),
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
            )
        ),
    )


# DragEvent: https://developer.mozilla.org/en-US/docs/Web/API/DragEvent
@dataclasses.dataclass
class DragEvent(MouseEvent):
    """Represents events that occur when an element or text selection is being dragged and dropped."""

    dataTransfer: str = ""  # Data being transferred (serialized as string)


def drag_event_spec(ev: rx.Var[DragEvent]) -> tuple[rx.Var[DragEvent]]:
    return (
        rx.Var.create(DragEvent(**dataclasses.asdict(mouse_event_spec(ev)[0].get()), dataTransfer=ev.dataTransfer)),
    )


@dataclasses.dataclass
class DragEnterEvent(DragEvent):
    """Represents a dragenter event (when a dragged item enters a valid drop target)."""

    pass


def drag_enter_event_spec(ev: rx.Var[DragEnterEvent]) -> tuple[rx.Var[DragEnterEvent]]:
    return (rx.Var.create(DragEnterEvent(**dataclasses.asdict(drag_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class DragLeaveEvent(DragEvent):
    """Represents a dragleave event (when a dragged item leaves a valid drop target)."""

    pass


def drag_leave_event_spec(ev: rx.Var[DragLeaveEvent]) -> tuple[rx.Var[DragLeaveEvent]]:
    return (rx.Var.create(DragLeaveEvent(**dataclasses.asdict(drag_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class DragOverEvent(DragEvent):
    """Represents a dragover event (when a dragged item is over a valid drop target)."""

    pass


def drag_over_event_spec(ev: rx.Var[DragOverEvent]) -> tuple[rx.Var[DragOverEvent]]:
    return (rx.Var.create(DragOverEvent(**dataclasses.asdict(drag_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class DragStartEvent(DragEvent):
    """Represents a dragstart event (when the user starts dragging an element or text selection)."""

    pass


def drag_start_event_spec(ev: rx.Var[DragStartEvent]) -> tuple[rx.Var[DragStartEvent]]:
    return (rx.Var.create(DragStartEvent(**dataclasses.asdict(drag_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class DragEndEvent(DragEvent):
    """Represents a dragend event (when a drag operation is ended by releasing the mouse button or hitting escape)."""

    pass


def drag_end_event_spec(ev: rx.Var[DragEndEvent]) -> tuple[rx.Var[DragEndEvent]]:
    return (rx.Var.create(DragEndEvent(**dataclasses.asdict(drag_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class DropEvent(DragEvent):
    """Represents a drop event (when a dragged item is dropped on a valid drop target)."""

    pass


def drop_event_spec(ev: rx.Var[DropEvent]) -> tuple[rx.Var[DropEvent]]:
    return (rx.Var.create(DropEvent(**dataclasses.asdict(drag_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class DoubleClickEvent(MouseEvent):
    """Represents a dblclick event."""

    pass


def double_click_event_spec(ev: rx.Var[DoubleClickEvent]) -> tuple[rx.Var[DoubleClickEvent]]:
    return (rx.Var.create(DoubleClickEvent(**dataclasses.asdict(mouse_event_spec(ev)[0].get()))),)
