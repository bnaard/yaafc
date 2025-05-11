"""
Mouse and pointer event dataclasses and event spec functions for DOM event handling.

This module provides Python representations of all major mouse-related DOM events, including mouse, wheel, pointer, and drag events, as well as their event spec functions for use with Reflex event handlers.
"""

import dataclasses

import reflex as rx
from reflex.vars.object import ObjectVar


@dataclasses.dataclass
class MouseEvent:
    """
    Represents events that occur due to the user interacting with a pointing device (mouse, pen, etc.).

    Attributes:
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


def mouse_event_spec(ev: ObjectVar[MouseEvent]) -> tuple[rx.Var[MouseEvent]]:
    """
    Event spec for MouseEvent, used to extract event data for Reflex event handlers.

    Args:
        ev: The MouseEvent variable from the event system.
    Returns:
        A tuple containing a Reflex Var of MouseEvent.
    """
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


@dataclasses.dataclass
class WheelEvent(MouseEvent):
    """
    Represents events that occur when the mouse wheel is rotated.

    Attributes:
        deltaX (float): Amount of horizontal scroll
        deltaY (float): Amount of vertical scroll
        deltaZ (float): Amount of z-axis scroll
        deltaMode (int): Unit of delta values (0=pixels, 1=lines, 2=pages)
    """

    deltaX: float = 0.0
    deltaY: float = 0.0
    deltaZ: float = 0.0
    deltaMode: int = 0


def wheel_event_spec(ev: rx.Var[WheelEvent]) -> tuple[rx.Var[WheelEvent]]:
    """
    Event spec for WheelEvent, used to extract event data for Reflex event handlers.

    Args:
        ev: The WheelEvent variable from the event system.
    Returns:
        A tuple containing a Reflex Var of WheelEvent.
    """
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


@dataclasses.dataclass
class PointerEvent(MouseEvent):
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


def pointer_event_spec(ev: rx.Var[PointerEvent]) -> tuple[rx.Var[PointerEvent]]:
    """
    Event spec for PointerEvent, used to extract event data for Reflex event handlers.

    Args:
        ev: The PointerEvent variable from the event system.
    Returns:
        A tuple containing a Reflex Var of PointerEvent.
    """
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


@dataclasses.dataclass
class DragEvent(MouseEvent):
    """
    Represents events that occur when an element or text selection is being dragged and dropped.

    Attributes:
        dataTransfer (str): Data being transferred (serialized as string)
    """

    dataTransfer: str = ""


def drag_event_spec(ev: rx.Var[DragEvent]) -> tuple[rx.Var[DragEvent]]:
    """
    Event spec for DragEvent, used to extract event data for Reflex event handlers.

    Args:
        ev: The DragEvent variable from the event system.
    Returns:
        A tuple containing a Reflex Var of DragEvent.
    """
    return (
        rx.Var.create(DragEvent(**dataclasses.asdict(mouse_event_spec(ev)[0].get()), dataTransfer=ev.dataTransfer)),
    )


@dataclasses.dataclass
class DragEnterEvent(DragEvent):
    """
    Represents a dragenter event (when a dragged item enters a valid drop target).
    Inherits all attributes from DragEvent.
    """

    pass


def drag_enter_event_spec(ev: rx.Var[DragEnterEvent]) -> tuple[rx.Var[DragEnterEvent]]:
    """
    Event spec for DragEnterEvent, used to extract event data for Reflex event handlers.
    Args:
        ev: The DragEnterEvent variable from the event system.
    Returns:
        A tuple containing a Reflex Var of DragEnterEvent.
    """
    return (rx.Var.create(DragEnterEvent(**dataclasses.asdict(drag_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class DragLeaveEvent(DragEvent):
    """
    Represents a dragleave event (when a dragged item leaves a valid drop target).
    Inherits all attributes from DragEvent.
    """

    pass


def drag_leave_event_spec(ev: rx.Var[DragLeaveEvent]) -> tuple[rx.Var[DragLeaveEvent]]:
    """
    Event spec for DragLeaveEvent, used to extract event data for Reflex event handlers.
    Args:
        ev: The DragLeaveEvent variable from the event system.
    Returns:
        A tuple containing a Reflex Var of DragLeaveEvent.
    """
    return (rx.Var.create(DragLeaveEvent(**dataclasses.asdict(drag_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class DragOverEvent(DragEvent):
    """
    Represents a dragover event (when a dragged item is over a valid drop target).
    Inherits all attributes from DragEvent.
    """

    pass


def drag_over_event_spec(ev: rx.Var[DragOverEvent]) -> tuple[rx.Var[DragOverEvent]]:
    """
    Event spec for DragOverEvent, used to extract event data for Reflex event handlers.
    Args:
        ev: The DragOverEvent variable from the event system.
    Returns:
        A tuple containing a Reflex Var of DragOverEvent.
    """
    return (rx.Var.create(DragOverEvent(**dataclasses.asdict(drag_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class DragStartEvent(DragEvent):
    """
    Represents a dragstart event (when the user starts dragging an element or text selection).
    Inherits all attributes from DragEvent.
    """

    pass


def drag_start_event_spec(ev: rx.Var[DragStartEvent]) -> tuple[rx.Var[DragStartEvent]]:
    """
    Event spec for DragStartEvent, used to extract event data for Reflex event handlers.
    Args:
        ev: The DragStartEvent variable from the event system.
    Returns:
        A tuple containing a Reflex Var of DragStartEvent.
    """
    return (rx.Var.create(DragStartEvent(**dataclasses.asdict(drag_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class DragEndEvent(DragEvent):
    """
    Represents a dragend event (when a drag operation is ended by releasing the mouse button or hitting escape).
    Inherits all attributes from DragEvent.
    """

    pass


def drag_end_event_spec(ev: rx.Var[DragEndEvent]) -> tuple[rx.Var[DragEndEvent]]:
    """
    Event spec for DragEndEvent, used to extract event data for Reflex event handlers.
    Args:
        ev: The DragEndEvent variable from the event system.
    Returns:
        A tuple containing a Reflex Var of DragEndEvent.
    """
    return (rx.Var.create(DragEndEvent(**dataclasses.asdict(drag_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class DropEvent(DragEvent):
    """
    Represents a drop event (when a dragged item is dropped on a valid drop target).
    Inherits all attributes from DragEvent.
    """

    pass


def drop_event_spec(ev: rx.Var[DropEvent]) -> tuple[rx.Var[DropEvent]]:
    """
    Event spec for DropEvent, used to extract event data for Reflex event handlers.
    Args:
        ev: The DropEvent variable from the event system.
    Returns:
        A tuple containing a Reflex Var of DropEvent.
    """
    return (rx.Var.create(DropEvent(**dataclasses.asdict(drag_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class DoubleClickEvent(MouseEvent):
    """
    Represents a dblclick event.
    Inherits all attributes from MouseEvent.
    """

    pass


def double_click_event_spec(ev: rx.Var[DoubleClickEvent]) -> tuple[rx.Var[DoubleClickEvent]]:
    """
    Event spec for DoubleClickEvent, used to extract event data for Reflex event handlers.
    Args:
        ev: The DoubleClickEvent variable from the event system.
    Returns:
        A tuple containing a Reflex Var of DoubleClickEvent.
    """
    return (rx.Var.create(DoubleClickEvent(**dataclasses.asdict(mouse_event_spec(ev)[0].get()))),)
