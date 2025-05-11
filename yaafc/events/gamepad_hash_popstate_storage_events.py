"""
Gamepad, hash, popstate, and storage event dataclasses and event spec functions for DOM event handling.

This module provides Python representations of gamepad, hashchange, popstate, and storage DOM events, including their event spec functions for use with Reflex event handlers.
"""

import dataclasses

import reflex as rx


# Gamepad: https://developer.mozilla.org/en-US/docs/Web/API/Gamepad
@dataclasses.dataclass
class Gamepad:
    """
    Represents a gamepad device.

    Attributes:
        id (str): Identifier for the gamepad
        index (int): Index of the gamepad
        connected (bool): Whether the gamepad is connected
        mapping (str): Mapping type
        axes (list): Axes values
        buttons (list): Button values
        timestamp (float): Last time the data was updated
    """

    id: str = ""  # Identifier for the gamepad
    index: int = 0  # Index of the gamepad
    connected: bool = False  # Whether the gamepad is connected
    mapping: str = ""  # Mapping type
    axes: list = dataclasses.field(default_factory=list)  # Axes values
    buttons: list = dataclasses.field(default_factory=list)  # Button values
    timestamp: float = 0.0  # Last time the data was updated


# GamepadEvent: https://developer.mozilla.org/en-US/docs/Web/API/GamepadEvent
@dataclasses.dataclass
class GamepadEvent:
    """
    Represents events providing information about gamepad connections and disconnections.

    Attributes:
        gamepad (Gamepad): The Gamepad object
    """

    gamepad: Gamepad = dataclasses.field(default_factory=Gamepad)  # The Gamepad object


def gamepad_event_spec(ev: rx.Var[GamepadEvent]) -> tuple[rx.Var[GamepadEvent]]:
    """
    Specifies the structure of a gamepad event.

    Args:
        ev (rx.Var[GamepadEvent]): The gamepad event variable.

    Returns:
        tuple[rx.Var[GamepadEvent]]: A tuple containing the gamepad event variable.
    """
    return (rx.Var.create(GamepadEvent(gamepad=ev.gamepad)),)


# HashChangeEvent: https://developer.mozilla.org/en-US/docs/Web/API/HashChangeEvent
@dataclasses.dataclass
class HashChangeEvent:
    """
    Represents events that are fired when the fragment identifier of the URL has changed.

    Attributes:
        oldURL (str): The previous URL
        newURL (str): The new URL
    """

    oldURL: str = ""  # The previous URL
    newURL: str = ""  # The new URL


def hash_change_event_spec(ev: rx.Var[HashChangeEvent]) -> tuple[rx.Var[HashChangeEvent]]:
    """
    Specifies the structure of a hash change event.

    Args:
        ev (rx.Var[HashChangeEvent]): The hash change event variable.

    Returns:
        tuple[rx.Var[HashChangeEvent]]: A tuple containing the hash change event variable.
    """
    return (rx.Var.create(HashChangeEvent(oldURL=ev.oldURL, newURL=ev.newURL)),)


# PopStateEvent: https://developer.mozilla.org/en-US/docs/Web/API/PopStateEvent
@dataclasses.dataclass
class PopStateEvent:
    """
    Represents events that are fired when the active history entry changes.

    Attributes:
        state (str): The state object associated with the history entry (serialized as string)
    """

    state: str = ""  # The state object associated with the history entry (serialized as string)


def pop_state_event_spec(ev: rx.Var[PopStateEvent]) -> tuple[rx.Var[PopStateEvent]]:
    """
    Specifies the structure of a pop state event.

    Args:
        ev (rx.Var[PopStateEvent]): The pop state event variable.

    Returns:
        tuple[rx.Var[PopStateEvent]]: A tuple containing the pop state event variable.
    """
    return (rx.Var.create(PopStateEvent(state=ev.state)),)


# Storage: https://developer.mozilla.org/en-US/docs/Web/API/Storage
@dataclasses.dataclass
class Storage:
    """
    Represents a storage area (localStorage or sessionStorage).

    Attributes:
        items (dict): Key/value pairs in storage
    """

    items: dict = dataclasses.field(default_factory=dict)  # Key/value pairs in storage


# StorageEvent: https://developer.mozilla.org/en-US/docs/Web/API/StorageEvent
@dataclasses.dataclass
class StorageEvent:
    """
    Represents events that are fired when a storage area changes.

    Attributes:
        key (str): The key changed
        oldValue (str): The old value of the key
        newValue (str): The new value of the key
        url (str): The URL of the document that changed the storage area
        storageArea (Storage): The Storage object
    """

    key: str = ""  # The key changed
    oldValue: str = ""  # The old value of the key
    newValue: str = ""  # The new value of the key
    url: str = ""  # The URL of the document that changed the storage area
    storageArea: Storage = dataclasses.field(default_factory=Storage)  # The Storage object


def storage_event_spec(ev: rx.Var[StorageEvent]) -> tuple[rx.Var[StorageEvent]]:
    """
    Specifies the structure of a storage event.

    Args:
        ev (rx.Var[StorageEvent]): The storage event variable.

    Returns:
        tuple[rx.Var[StorageEvent]]: A tuple containing the storage event variable.
    """
    return (
        rx.Var.create(
            StorageEvent(
                key=ev.key,
                oldValue=ev.oldValue,
                newValue=ev.newValue,
                url=ev.url,
                storageArea=ev.storageArea,
            )
        ),
    )
