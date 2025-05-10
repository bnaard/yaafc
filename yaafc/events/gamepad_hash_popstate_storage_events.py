import dataclasses

import reflex as rx


# Gamepad: https://developer.mozilla.org/en-US/docs/Web/API/Gamepad
@dataclasses.dataclass
class Gamepad:
    """Represents a gamepad device."""

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
    """Represents events providing information about gamepad connections and disconnections."""

    gamepad: Gamepad = dataclasses.field(default_factory=Gamepad)  # The Gamepad object


def gamepad_event_spec(ev: rx.Var[GamepadEvent]) -> tuple[rx.Var[GamepadEvent]]:
    return (rx.Var.create(GamepadEvent(gamepad=ev.gamepad)),)


# HashChangeEvent: https://developer.mozilla.org/en-US/docs/Web/API/HashChangeEvent
@dataclasses.dataclass
class HashChangeEvent:
    """Represents events that are fired when the fragment identifier of the URL has changed."""

    oldURL: str = ""  # The previous URL
    newURL: str = ""  # The new URL


def hash_change_event_spec(ev: rx.Var[HashChangeEvent]) -> tuple[rx.Var[HashChangeEvent]]:
    return (rx.Var.create(HashChangeEvent(oldURL=ev.oldURL, newURL=ev.newURL)),)


# PopStateEvent: https://developer.mozilla.org/en-US/docs/Web/API/PopStateEvent
@dataclasses.dataclass
class PopStateEvent:
    """Represents events that are fired when the active history entry changes."""

    state: str = ""  # The state object associated with the history entry (serialized as string)


def pop_state_event_spec(ev: rx.Var[PopStateEvent]) -> tuple[rx.Var[PopStateEvent]]:
    return (rx.Var.create(PopStateEvent(state=ev.state)),)


# Storage: https://developer.mozilla.org/en-US/docs/Web/API/Storage
@dataclasses.dataclass
class Storage:
    """Represents a storage area (localStorage or sessionStorage)."""

    items: dict = dataclasses.field(default_factory=dict)  # Key/value pairs in storage


# StorageEvent: https://developer.mozilla.org/en-US/docs/Web/API/StorageEvent
@dataclasses.dataclass
class StorageEvent:
    """Represents events that are fired when a storage area changes."""

    key: str = ""  # The key changed
    oldValue: str = ""  # The old value of the key
    newValue: str = ""  # The new value of the key
    url: str = ""  # The URL of the document that changed the storage area
    storageArea: Storage = dataclasses.field(default_factory=Storage)  # The Storage object


def storage_event_spec(ev: rx.Var[StorageEvent]) -> tuple[rx.Var[StorageEvent]]:
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
