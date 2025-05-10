import dataclasses

import reflex as rx


# BeforeUnloadEvent: https://developer.mozilla.org/en-US/docs/Web/API/BeforeUnloadEvent
@dataclasses.dataclass
class BeforeUnloadEvent:
    """Represents events that are fired before the window, document, and its resources are about to be unloaded."""

    returnValue: str = ""  # Message to display to the user


def before_unload_event_spec(ev: rx.Var[BeforeUnloadEvent]) -> tuple[rx.Var[BeforeUnloadEvent]]:
    """
    Returns a tuple of all BeforeUnloadEvent properties, in the same order as the dataclass.
    """
    return (rx.Var.create(BeforeUnloadEvent(returnValue=ev.returnValue)),)


# PageTransitionEvent: https://developer.mozilla.org/en-US/docs/Web/API/PageTransitionEvent
@dataclasses.dataclass
class PageTransitionEvent:
    """Represents events sent when a document is being loaded or unloaded."""

    persisted: bool = False  # True if the page is being persisted in the session history


def page_transition_event_spec(ev: rx.Var[PageTransitionEvent]) -> tuple[rx.Var[PageTransitionEvent]]:
    """
    Returns a tuple of all PageTransitionEvent properties, in the same order as the dataclass.
    """
    return (rx.Var.create(PageTransitionEvent(persisted=ev.persisted)),)
