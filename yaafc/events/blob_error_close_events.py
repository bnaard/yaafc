"""
Blob, error, and close event dataclasses and event spec functions for DOM event handling.

This module provides Python representations of Blob, Error, and Close DOM events, including their event spec functions for use with Reflex event handlers.
"""

import dataclasses

import reflex as rx


# Blob: https://developer.mozilla.org/en-US/docs/Web/API/Blob
@dataclasses.dataclass
class Blob:
    """
    Represents immutable raw binary data.

    Attributes:
        size (int): Size of the blob in bytes
        type (str): MIME type of the blob
    """

    size: int = 0  # Size of the blob in bytes
    type: str = ""  # MIME type of the blob
    # Note: In browsers, Blob has methods (slice, etc.), but for event data, only metadata is relevant.


# BlobEvent: https://developer.mozilla.org/en-US/docs/Web/API/BlobEvent
@dataclasses.dataclass
class BlobEvent:
    """
    Represents events that provide access to Blob data (e.g., from MediaRecorder).

    Attributes:
        data (Blob): The Blob object
        timecode (float): The timecode of the Blob data
    """

    data: Blob = dataclasses.field(default_factory=Blob)  # The Blob object
    timecode: float = 0.0  # The timecode of the Blob data


def blob_event_spec(ev: rx.Var[BlobEvent]) -> tuple[rx.Var[BlobEvent]]:
    """
    Event spec function for BlobEvent.

    Args:
        ev (rx.Var[BlobEvent]): The BlobEvent variable.

    Returns:
        tuple[rx.Var[BlobEvent]]: A tuple containing the BlobEvent variable.
    """
    return (rx.Var.create(BlobEvent(data=ev.data, timecode=ev.timecode)),)


# Error: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error
@dataclasses.dataclass
class Error:
    """
    Represents a JavaScript error object.

    Attributes:
        name (str): Name of the error
        message (str): Error message
        stack (str): Stack trace
    """

    name: str = ""  # Name of the error
    message: str = ""  # Error message
    stack: str = ""  # Stack trace


# ErrorEvent: https://developer.mozilla.org/en-US/docs/Web/API/ErrorEvent
@dataclasses.dataclass
class ErrorEvent:
    """
    Represents events providing information about errors that occur in scripts.

    Attributes:
        message (str): Error message
        filename (str): Name of the script file
        lineno (int): Line number where the error occurred
        colno (int): Column number where the error occurred
        error (Error): The actual error object
    """

    message: str = ""  # Error message
    filename: str = ""  # Name of the script file
    lineno: int = 0  # Line number where the error occurred
    colno: int = 0  # Column number where the error occurred
    error: Error = dataclasses.field(default_factory=Error)  # The actual error object


def error_event_spec(ev: rx.Var[ErrorEvent]) -> tuple[rx.Var[ErrorEvent]]:
    """
    Event spec function for ErrorEvent.

    Args:
        ev (rx.Var[ErrorEvent]): The ErrorEvent variable.

    Returns:
        tuple[rx.Var[ErrorEvent]]: A tuple containing the ErrorEvent variable.
    """
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
    """
    Represents events signaling that a WebSocket connection has been closed.

    Attributes:
        was_clean (bool): True if the connection was closed cleanly
        code (int): The WebSocket connection close code
        reason (str): Reason for closing the connection
    """

    was_clean: bool = False  # True if the connection was closed cleanly
    code: int = 0  # The WebSocket connection close code
    reason: str = ""  # Reason for closing the connection


def close_event_spec(ev: rx.Var[CloseEvent]) -> tuple[rx.Var[CloseEvent]]:
    """
    Event spec function for CloseEvent.

    Args:
        ev (rx.Var[CloseEvent]): The CloseEvent variable.

    Returns:
        tuple[rx.Var[CloseEvent]]: A tuple containing the CloseEvent variable.
    """
    return (
        rx.Var.create(
            CloseEvent(
                was_clean=ev.was_clean,
                code=ev.code,
                reason=ev.reason,
            )
        ),
    )
