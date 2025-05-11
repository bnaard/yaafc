"""
Keyboard and composition event dataclasses and event spec functions for DOM event handling.

This module provides Python representations of keyboard and composition DOM events, including their event spec functions for use with Reflex event handlers.
"""

import dataclasses

import reflex as rx


# KeyboardEvent: https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent
@dataclasses.dataclass
class KeyboardEvent:
    """
    Represents events that occur due to the user interacting with a keyboard.

    Attributes:
        altKey (bool): True if Alt key was pressed
        code (str): Physical key code
        ctrlKey (bool): True if Ctrl key was pressed
        isComposing (bool): True if event is part of IME composition
        key (str): Value of the key pressed
        location (int): Location of the key on the device
        metaKey (bool): True if Meta (Cmd) key was pressed
        repeat (bool): True if key is being held down
        shiftKey (bool): True if Shift key was pressed
    """

    altKey: bool = False
    code: str = ""
    ctrlKey: bool = False
    isComposing: bool = False
    key: str = ""
    location: int = 0
    metaKey: bool = False
    repeat: bool = False
    shiftKey: bool = False


def keyboard_event_spec(ev: rx.Var[KeyboardEvent]) -> tuple[rx.Var[KeyboardEvent]]:
    """
    Event spec function for KeyboardEvent.

    Args:
        ev (rx.Var[KeyboardEvent]): The KeyboardEvent variable.

    Returns:
        tuple[rx.Var[KeyboardEvent]]: A tuple containing the KeyboardEvent variable.
    """
    return (
        rx.Var.create(
            KeyboardEvent(
                altKey=ev.altKey,
                code=ev.code,
                ctrlKey=ev.ctrlKey,
                isComposing=ev.isComposing,
                key=ev.key,
                location=ev.location,
                metaKey=ev.metaKey,
                repeat=ev.repeat,
                shiftKey=ev.shiftKey,
            )
        ),
    )


@dataclasses.dataclass
class KeyDownEvent(KeyboardEvent):
    """
    Represents a keydown event.
    Inherits all attributes from KeyboardEvent.
    """

    pass


def key_down_event_spec(ev: rx.Var[KeyDownEvent]) -> tuple[rx.Var[KeyDownEvent]]:
    """
    Event spec function for KeyDownEvent.

    Args:
        ev (rx.Var[KeyDownEvent]): The KeyDownEvent variable.

    Returns:
        tuple[rx.Var[KeyDownEvent]]: A tuple containing the KeyDownEvent variable.
    """
    return (rx.Var.create(KeyDownEvent(**dataclasses.asdict(keyboard_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class KeyUpEvent(KeyboardEvent):
    """
    Represents a keyup event.
    Inherits all attributes from KeyboardEvent.
    """

    pass


def key_up_event_spec(ev: rx.Var[KeyUpEvent]) -> tuple[rx.Var[KeyUpEvent]]:
    """
    Event spec function for KeyUpEvent.

    Args:
        ev (rx.Var[KeyUpEvent]): The KeyUpEvent variable.

    Returns:
        tuple[rx.Var[KeyUpEvent]]: A tuple containing the KeyUpEvent variable.
    """
    return (rx.Var.create(KeyUpEvent(**dataclasses.asdict(keyboard_event_spec(ev)[0].get()))),)


# InputEvent: https://developer.mozilla.org/en-US/docs/Web/API/InputEvent
@dataclasses.dataclass
class InputEvent:
    """
    Represents events that occur when the value of an <input>, <select>, or <textarea> element is changed.

    Attributes:
        data (str): The inserted or deleted data
        inputType (str): The type of change (e.g., 'insertText')
        isComposing (bool): True if event is part of IME composition
    """

    data: str = ""
    inputType: str = ""
    isComposing: bool = False


def input_event_spec(ev: rx.Var[InputEvent]) -> tuple[rx.Var[InputEvent]]:
    """
    Event spec function for InputEvent.

    Args:
        ev (rx.Var[InputEvent]): The InputEvent variable.

    Returns:
        tuple[rx.Var[InputEvent]]: A tuple containing the InputEvent variable.
    """
    return (
        rx.Var.create(
            InputEvent(
                data=ev.data,
                inputType=ev.inputType,
                isComposing=ev.isComposing,
            )
        ),
    )


@dataclasses.dataclass
class BeforeInputEvent(InputEvent):
    """
    Represents a beforeinput event.
    Inherits all attributes from InputEvent.
    """

    pass


def before_input_event_spec(ev: rx.Var[BeforeInputEvent]) -> tuple[rx.Var[BeforeInputEvent]]:
    """
    Event spec function for BeforeInputEvent.

    Args:
        ev (rx.Var[BeforeInputEvent]): The BeforeInputEvent variable.

    Returns:
        tuple[rx.Var[BeforeInputEvent]]: A tuple containing the BeforeInputEvent variable.
    """
    return (rx.Var.create(BeforeInputEvent(**dataclasses.asdict(input_event_spec(ev)[0].get()))),)


# CompositionEvent: https://developer.mozilla.org/en-US/docs/Web/API/CompositionEvent
@dataclasses.dataclass
class CompositionEvent:
    """
    Represents events that occur due to the user indirectly entering text (e.g., IME).

    Attributes:
        data (str): The characters generated by the input method
    """

    data: str = ""


def composition_event_spec(ev: rx.Var[CompositionEvent]) -> tuple[rx.Var[CompositionEvent]]:
    """
    Event spec function for CompositionEvent.

    Args:
        ev (rx.Var[CompositionEvent]): The CompositionEvent variable.

    Returns:
        tuple[rx.Var[CompositionEvent]]: A tuple containing the CompositionEvent variable.
    """
    return (rx.Var.create(CompositionEvent(data=ev.data)),)


@dataclasses.dataclass
class CompositionEndEvent(CompositionEvent):
    """
    Represents a compositionend event.
    Inherits all attributes from CompositionEvent.
    """

    pass


def composition_end_event_spec(ev: rx.Var[CompositionEndEvent]) -> tuple[rx.Var[CompositionEndEvent]]:
    """
    Event spec function for CompositionEndEvent.

    Args:
        ev (rx.Var[CompositionEndEvent]): The CompositionEndEvent variable.

    Returns:
        tuple[rx.Var[CompositionEndEvent]]: A tuple containing the CompositionEndEvent variable.
    """
    return composition_event_spec(ev)


@dataclasses.dataclass
class CompositionStartEvent(CompositionEvent):
    """
    Represents a compositionstart event.
    Inherits all attributes from CompositionEvent.
    """

    pass


def composition_start_event_spec(ev: rx.Var[CompositionStartEvent]) -> tuple[rx.Var[CompositionStartEvent]]:
    """
    Event spec function for CompositionStartEvent.

    Args:
        ev (rx.Var[CompositionStartEvent]): The CompositionStartEvent variable.

    Returns:
        tuple[rx.Var[CompositionStartEvent]]: A tuple containing the CompositionStartEvent variable.
    """
    return composition_event_spec(ev)


@dataclasses.dataclass
class CompositionUpdateEvent(CompositionEvent):
    """
    Represents a compositionupdate event.
    Inherits all attributes from CompositionEvent.
    """

    pass


def composition_update_event_spec(ev: rx.Var[CompositionUpdateEvent]) -> tuple[rx.Var[CompositionUpdateEvent]]:
    """
    Event spec function for CompositionUpdateEvent.

    Args:
        ev (rx.Var[CompositionUpdateEvent]): The CompositionUpdateEvent variable.

    Returns:
        tuple[rx.Var[CompositionUpdateEvent]]: A tuple containing the CompositionUpdateEvent variable.
    """
    return composition_event_spec(ev)
