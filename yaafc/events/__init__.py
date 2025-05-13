"""
Event dataclasses and spec functions for all major DOM event types, following MDN documentation.

This module provides Python representations of the corresponding DOM events and their data objects, clustered by event type.

Exports all event dataclasses and spec functions from submodules.
"""

from .animation_transition_events import (
    AnimationEndEvent,
    AnimationEvent,
    AnimationIterationEvent,
    AnimationStartEvent,
    TransitionEvent,
    WebGLContextEvent,
)
from .blob_error_close_events import (
    Blob,
    BlobEvent,
    CloseEvent,
    Error,
    ErrorEvent,
)
from .clipboard_events import (
    ClipboardEvent,
    CopyEvent,
    CutEvent,
    PasteEvent,
)
from .custom_events import CustomEvent
from .enhanced_event_watcher import EnhancedEventWatcher, enhanced_event_watcher
from .fetch_form_submit_events import (
    FetchEvent,
    FormData,
    FormDataEvent,
    Request,
    SubmitEvent,
)
from .focus_events import BlurEvent, FocusEvent, FocusInEvent
from .gamepad_hash_popstate_storage_events import (
    Gamepad,
    GamepadEvent,
    HashChangeEvent,
    PopStateEvent,
    Storage,
    StorageEvent,
)
from .generic_events import (
    Event,
    ProgressEvent,
    SecurityPolicyViolationEvent,
)
from .keyboard_events import (
    BeforeInputEvent,
    CompositionEndEvent,
    CompositionEvent,
    CompositionStartEvent,
    CompositionUpdateEvent,
    InputEvent,
    KeyboardEvent,
    KeyDownEvent,
    KeyUpEvent,
)
from .mouse_events import (
    DoubleClickEvent,
    DragEndEvent,
    DragEnterEvent,
    DragEvent,
    DragLeaveEvent,
    DragOverEvent,
    DragStartEvent,
    DropEvent,
    MouseEvent,
    PointerEvent,
    WheelEvent,
)
from .pointer_events import (
    GotPointerCaptureEvent,
    LostPointerCaptureEvent,
    PointerCancelEvent,
    PointerDownEvent,
    PointerEnterEvent,
    PointerLeaveEvent,
    PointerMoveEvent,
    PointerOutEvent,
    PointerOverEvent,
    PointerUpEvent,
)
from .touch_events import TouchEvent
from .ui_events import ScrollEndEvent, ScrollEvent, UIEvent
from .unload_transition_events import (
    BeforeUnloadEvent,
    PageTransitionEvent,
)

__all__ = [
    "AnimationEndEvent",
    # animation_transition_events
    "AnimationEvent",
    "AnimationIterationEvent",
    "AnimationStartEvent",
    "BeforeInputEvent",
    # unload_transition_events
    "BeforeUnloadEvent",
    # blob_error_close_events
    "Blob",
    "BlobEvent",
    "BlurEvent",
    # clipboard_events
    "ClipboardEvent",
    "CloseEvent",
    "CompositionEndEvent",
    "CompositionEvent",
    "CompositionStartEvent",
    "CompositionUpdateEvent",
    "CopyEvent",
    # custom_events
    "CustomEvent",
    "CutEvent",
    "DoubleClickEvent",
    "DragEndEvent",
    "DragEnterEvent",
    "DragEvent",
    "DragLeaveEvent",
    "DragOverEvent",
    "DragStartEvent",
    "DropEvent",
    "EnhancedEventWatcher",
    "Error",
    "ErrorEvent",
    # generic_events
    "Event",
    "FetchEvent",
    # focus_events
    "FocusEvent",
    "FocusInEvent",
    "FormData",
    "FormDataEvent",
    # gamepad_hash_popstate_storage_events
    "Gamepad",
    "GamepadEvent",
    # pointer_events
    "GotPointerCaptureEvent",
    "HashChangeEvent",
    "InputEvent",
    "KeyDownEvent",
    "KeyUpEvent",
    # keyboard_events
    "KeyboardEvent",
    "LostPointerCaptureEvent",
    # mouse_events
    "MouseEvent",
    "PageTransitionEvent",
    "PasteEvent",
    "PointerCancelEvent",
    "PointerDownEvent",
    "PointerEnterEvent",
    "PointerEvent",
    "PointerLeaveEvent",
    "PointerMoveEvent",
    "PointerOutEvent",
    "PointerOverEvent",
    "PointerUpEvent",
    "PopStateEvent",
    "ProgressEvent",
    # fetch_form_submit_events
    "Request",
    "ScrollEndEvent",
    "ScrollEvent",
    "SecurityPolicyViolationEvent",
    "Storage",
    "StorageEvent",
    "SubmitEvent",
    # touch_events
    "TouchEvent",
    "TransitionEvent",
    # ui_events
    "UIEvent",
    "WebGLContextEvent",
    "WheelEvent",
    "enhanced_event_watcher",
]
