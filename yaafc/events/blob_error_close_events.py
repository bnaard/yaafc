import dataclasses

import reflex as rx


# Blob: https://developer.mozilla.org/en-US/docs/Web/API/Blob
@dataclasses.dataclass
class Blob:
    """Represents immutable raw binary data."""

    size: int = 0  # Size of the blob in bytes
    type: str = ""  # MIME type of the blob
    # Note: In browsers, Blob has methods (slice, etc.), but for event data, only metadata is relevant.


# BlobEvent: https://developer.mozilla.org/en-US/docs/Web/API/BlobEvent
@dataclasses.dataclass
class BlobEvent:
    """Represents events that provide access to Blob data (e.g., from MediaRecorder)."""

    data: Blob = dataclasses.field(default_factory=Blob)  # The Blob object
    timecode: float = 0.0  # The timecode of the Blob data


def blob_event_spec(ev: rx.Var[BlobEvent]) -> tuple[rx.Var[BlobEvent]]:
    return (rx.Var.create(BlobEvent(data=ev.data, timecode=ev.timecode)),)


# Error: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error
@dataclasses.dataclass
class Error:
    """Represents a JavaScript error object."""

    name: str = ""  # Name of the error
    message: str = ""  # Error message
    stack: str = ""  # Stack trace


# ErrorEvent: https://developer.mozilla.org/en-US/docs/Web/API/ErrorEvent
@dataclasses.dataclass
class ErrorEvent:
    """Represents events providing information about errors that occur in scripts."""

    message: str = ""  # Error message
    filename: str = ""  # Name of the script file
    lineno: int = 0  # Line number where the error occurred
    colno: int = 0  # Column number where the error occurred
    error: Error = dataclasses.field(default_factory=Error)  # The actual error object


def error_event_spec(ev: rx.Var[ErrorEvent]) -> tuple[rx.Var[ErrorEvent]]:
    return (
        rx.Var.create(
            ErrorEvent(
                message=ev.message,
                filename=ev.filename,
                lineno=ev.lineno,
                colno=ev.colno,
                error=ev.error,
            )
        ),
    )


# CloseEvent: https://developer.mozilla.org/en-US/docs/Web/API/CloseEvent
@dataclasses.dataclass
class CloseEvent:
    """Represents events signaling that a WebSocket connection has been closed."""

    was_clean: bool = False  # True if the connection was closed cleanly
    code: int = 0  # The WebSocket connection close code
    reason: str = ""  # Reason for closing the connection


def close_event_spec(ev: rx.Var[CloseEvent]) -> tuple[rx.Var[CloseEvent]]:
    return (
        rx.Var.create(
            CloseEvent(
                was_clean=ev.was_clean,
                code=ev.code,
                reason=ev.reason,
            )
        ),
    )
