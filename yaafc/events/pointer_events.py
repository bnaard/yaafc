"""
Pointer event dataclasses and event spec functions for DOM event handling.

This module provides Python representations of pointer-related DOM events, including their event spec functions for use with Reflex event handlers.
"""

import dataclasses

import reflex as rx


@dataclasses.dataclass
class PointerEvent:
    """
    Represents events that occur when a pointer (mouse, pen, touch, etc.) interacts with the surface.

    Attributes:
        pointerId (int): Unique ID for the pointer
        width (float): Width of the pointer's contact geometry
        height (float): Height of the pointer's contact geometry
        pressure (float): Pressure of the pointer
        tangentialPressure (float): Tangential pressure
        tiltX (int): Tilt of the pointer in X
        tiltY (int): Tilt of the pointer in Y
        twist (int): Rotation of the pointer
        pointerType (str): Type of pointer (mouse, pen, touch)
        isPrimary (bool): True if primary pointer
        altKey (bool): True if Alt key was pressed
        button (int): Which button was pressed (0=left, 1=middle, 2=right)
        buttons (int): Bitfield of buttons currently pressed
        clientX (int): X coordinate in viewport
        clientY (int): Y coordinate in viewport
        ctrlKey (bool): True if Ctrl key was pressed
        metaKey (bool): True if Meta (Cmd) key was pressed
        movementX (int): X movement since last event
        movementY (int): Y movement since last event
        offsetX (int): X relative to target element
        offsetY (int): Y relative to target element
        pageX (int): X relative to document
        pageY (int): Y relative to document
        relatedTarget (str): Secondary target (e.g., for mouseover/out)
        screenX (int): X relative to screen
        screenY (int): Y relative to screen
        shiftKey (bool): True if Shift key was pressed
        detail (int): Number of consecutive clicks
    """

    pointerId: int = 0
    width: float = 1.0
    height: float = 1.0
    pressure: float = 0.0
    tangentialPressure: float = 0.0
    tiltX: int = 0
    tiltY: int = 0
    twist: int = 0
    pointerType: str = "mouse"
    isPrimary: bool = True
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
    """
    Creates a specification for a PointerEvent.

    Args:
        ev (rx.Var[PointerEvent]): The PointerEvent variable.

    Returns:
        tuple[rx.Var[PointerEvent]]: A tuple containing the PointerEvent variable.
    """
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
    """
    Represents a gotpointercapture event.
    Inherits all attributes from PointerEvent.
    """

    pass


def got_pointer_capture_event_spec(ev: rx.Var[GotPointerCaptureEvent]) -> tuple[rx.Var[GotPointerCaptureEvent]]:
    """
    Creates a specification for a GotPointerCaptureEvent.

    Args:
        ev (rx.Var[GotPointerCaptureEvent]): The GotPointerCaptureEvent variable.

    Returns:
        tuple[rx.Var[GotPointerCaptureEvent]]: A tuple containing the GotPointerCaptureEvent variable.
    """
    return (rx.Var.create(GotPointerCaptureEvent(**dataclasses.asdict(pointer_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class LostPointerCaptureEvent(PointerEvent):
    """
    Represents a lostpointercapture event.
    Inherits all attributes from PointerEvent.
    """

    pass


def lost_pointer_capture_event_spec(ev: rx.Var[LostPointerCaptureEvent]) -> tuple[rx.Var[LostPointerCaptureEvent]]:
    """
    Creates a specification for a LostPointerCaptureEvent.

    Args:
        ev (rx.Var[LostPointerCaptureEvent]): The LostPointerCaptureEvent variable.

    Returns:
        tuple[rx.Var[LostPointerCaptureEvent]]: A tuple containing the LostPointerCaptureEvent variable.
    """
    return (rx.Var.create(LostPointerCaptureEvent(**dataclasses.asdict(pointer_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class PointerCancelEvent(PointerEvent):
    """
    Represents a pointercancel event.
    Inherits all attributes from PointerEvent.
    """

    pass


def pointer_cancel_event_spec(ev: rx.Var[PointerCancelEvent]) -> tuple[rx.Var[PointerCancelEvent]]:
    """
    Creates a specification for a PointerCancelEvent.

    Args:
        ev (rx.Var[PointerCancelEvent]): The PointerCancelEvent variable.

    Returns:
        tuple[rx.Var[PointerCancelEvent]]: A tuple containing the PointerCancelEvent variable.
    """
    return (rx.Var.create(PointerCancelEvent(**dataclasses.asdict(pointer_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class PointerDownEvent(PointerEvent):
    """
    Represents a pointerdown event.
    Inherits all attributes from PointerEvent.
    """

    pass


def pointer_down_event_spec(ev: rx.Var[PointerDownEvent]) -> tuple[rx.Var[PointerDownEvent]]:
    """
    Creates a specification for a PointerDownEvent.

    Args:
        ev (rx.Var[PointerDownEvent]): The PointerDownEvent variable.

    Returns:
        tuple[rx.Var[PointerDownEvent]]: A tuple containing the PointerDownEvent variable.
    """
    return (rx.Var.create(PointerDownEvent(**dataclasses.asdict(pointer_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class PointerEnterEvent(PointerEvent):
    """
    Represents a pointerenter event.
    Inherits all attributes from PointerEvent.
    """

    pass


def pointer_enter_event_spec(ev: rx.Var[PointerEnterEvent]) -> tuple[rx.Var[PointerEnterEvent]]:
    """
    Creates a specification for a PointerEnterEvent.

    Args:
        ev (rx.Var[PointerEnterEvent]): The PointerEnterEvent variable.

    Returns:
        tuple[rx.Var[PointerEnterEvent]]: A tuple containing the PointerEnterEvent variable.
    """
    return (rx.Var.create(PointerEnterEvent(**dataclasses.asdict(pointer_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class PointerLeaveEvent(PointerEvent):
    """
    Represents a pointerleave event.
    Inherits all attributes from PointerEvent.
    """

    pass


def pointer_leave_event_spec(ev: rx.Var[PointerLeaveEvent]) -> tuple[rx.Var[PointerLeaveEvent]]:
    """
    Creates a specification for a PointerLeaveEvent.

    Args:
        ev (rx.Var[PointerLeaveEvent]): The PointerLeaveEvent variable.

    Returns:
        tuple[rx.Var[PointerLeaveEvent]]: A tuple containing the PointerLeaveEvent variable.
    """
    return (rx.Var.create(PointerLeaveEvent(**dataclasses.asdict(pointer_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class PointerMoveEvent(PointerEvent):
    """
    Represents a pointermove event.
    Inherits all attributes from PointerEvent.
    """

    pass


def pointer_move_event_spec(ev: rx.Var[PointerMoveEvent]) -> tuple[rx.Var[PointerMoveEvent]]:
    """
    Creates a specification for a PointerMoveEvent.

    Args:
        ev (rx.Var[PointerMoveEvent]): The PointerMoveEvent variable.

    Returns:
        tuple[rx.Var[PointerMoveEvent]]: A tuple containing the PointerMoveEvent variable.
    """
    return (rx.Var.create(PointerMoveEvent(**dataclasses.asdict(pointer_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class PointerOutEvent(PointerEvent):
    """
    Represents a pointerout event.
    Inherits all attributes from PointerEvent.
    """

    pass


def pointer_out_event_spec(ev: rx.Var[PointerOutEvent]) -> tuple[rx.Var[PointerOutEvent]]:
    """
    Creates a specification for a PointerOutEvent.

    Args:
        ev (rx.Var[PointerOutEvent]): The PointerOutEvent variable.

    Returns:
        tuple[rx.Var[PointerOutEvent]]: A tuple containing the PointerOutEvent variable.
    """
    return (rx.Var.create(PointerOutEvent(**dataclasses.asdict(pointer_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class PointerOverEvent(PointerEvent):
    """
    Represents a pointerover event.
    Inherits all attributes from PointerEvent.
    """

    pass


def pointer_over_event_spec(ev: rx.Var[PointerOverEvent]) -> tuple[rx.Var[PointerOverEvent]]:
    """
    Creates a specification for a PointerOverEvent.

    Args:
        ev (rx.Var[PointerOverEvent]): The PointerOverEvent variable.

    Returns:
        tuple[rx.Var[PointerOverEvent]]: A tuple containing the PointerOverEvent variable.
    """
    return (rx.Var.create(PointerOverEvent(**dataclasses.asdict(pointer_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class PointerUpEvent(PointerEvent):
    """
    Represents a pointerup event.
    Inherits all attributes from PointerEvent.
    """

    pass


def pointer_up_event_spec(ev: rx.Var[PointerUpEvent]) -> tuple[rx.Var[PointerUpEvent]]:
    """
    Creates a specification for a PointerUpEvent.

    Args:
        ev (rx.Var[PointerUpEvent]): The PointerUpEvent variable.

    Returns:
        tuple[rx.Var[PointerUpEvent]]: A tuple containing the PointerUpEvent variable.
    """
    return (rx.Var.create(PointerUpEvent(**dataclasses.asdict(pointer_event_spec(ev)[0].get()))),)
