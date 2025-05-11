"""
Animation and transition event dataclasses and event spec functions for DOM event handling.

This module provides Python representations of animation and transition DOM events, including their event spec functions for use with Reflex event handlers.
"""

import dataclasses

import reflex as rx


# AnimationEvent: https://developer.mozilla.org/en-US/docs/Web/API/AnimationEvent
@dataclasses.dataclass
class AnimationEvent:
    """
    Represents events providing information about animations.

    Attributes:
        animationName (str): Name of the animation
        elapsedTime (float): Time the animation has been running (in seconds)
        pseudoElement (str): Pseudo-element the animation applies to
    """

    animationName: str = ""  # Name of the animation
    elapsedTime: float = 0.0  # Time the animation has been running (in seconds)
    pseudoElement: str = ""  # Pseudo-element the animation applies to


def animation_event_spec(ev: rx.Var[AnimationEvent]) -> tuple[rx.Var[AnimationEvent]]:
    """
    Creates a specification for an AnimationEvent.

    Args:
        ev (rx.Var[AnimationEvent]): The AnimationEvent variable.

    Returns:
        tuple[rx.Var[AnimationEvent]]: A tuple containing the AnimationEvent specification.
    """
    return (
        rx.Var.create(
            AnimationEvent(
                animationName=ev.animationName,
                elapsedTime=ev.elapsedTime,
                pseudoElement=ev.pseudoElement,
            )
        ),
    )


@dataclasses.dataclass
class AnimationEndEvent(AnimationEvent):
    """
    Represents an animationend event.
    Inherits all attributes from AnimationEvent.
    """

    pass


def animation_end_event_spec(ev: rx.Var[AnimationEndEvent]) -> tuple[rx.Var[AnimationEndEvent]]:
    """
    Creates a specification for an AnimationEndEvent.

    Args:
        ev (rx.Var[AnimationEndEvent]): The AnimationEndEvent variable.

    Returns:
        tuple[rx.Var[AnimationEndEvent]]: A tuple containing the AnimationEndEvent specification.
    """
    return (rx.Var.create(AnimationEndEvent(**dataclasses.asdict(animation_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class AnimationIterationEvent(AnimationEvent):
    """
    Represents an animationiteration event.
    Inherits all attributes from AnimationEvent.
    """

    pass


def animation_iteration_event_spec(ev: rx.Var[AnimationIterationEvent]) -> tuple[rx.Var[AnimationIterationEvent]]:
    """
    Creates a specification for an AnimationIterationEvent.

    Args:
        ev (rx.Var[AnimationIterationEvent]): The AnimationIterationEvent variable.

    Returns:
        tuple[rx.Var[AnimationIterationEvent]]: A tuple containing the AnimationIterationEvent specification.
    """
    return (rx.Var.create(AnimationIterationEvent(**dataclasses.asdict(animation_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class AnimationStartEvent(AnimationEvent):
    """
    Represents an animationstart event.
    Inherits all attributes from AnimationEvent.
    """

    pass


def animation_start_event_spec(ev: rx.Var[AnimationStartEvent]) -> tuple[rx.Var[AnimationStartEvent]]:
    """
    Creates a specification for an AnimationStartEvent.

    Args:
        ev (rx.Var[AnimationStartEvent]): The AnimationStartEvent variable.

    Returns:
        tuple[rx.Var[AnimationStartEvent]]: A tuple containing the AnimationStartEvent specification.
    """
    return (rx.Var.create(AnimationStartEvent(**dataclasses.asdict(animation_event_spec(ev)[0].get()))),)


# TransitionEvent: https://developer.mozilla.org/en-US/docs/Web/API/TransitionEvent
@dataclasses.dataclass
class TransitionEvent:
    """
    Represents events providing information about CSS transitions.

    Attributes:
        propertyName (str): Name of the CSS property transitioning
        elapsedTime (float): Time the transition has been running (in seconds)
        pseudoElement (str): Pseudo-element the transition applies to
    """

    propertyName: str = ""  # Name of the CSS property transitioning
    elapsedTime: float = 0.0  # Time the transition has been running (in seconds)
    pseudoElement: str = ""  # Pseudo-element the transition applies to


def transition_event_spec(ev: rx.Var[TransitionEvent]) -> tuple[rx.Var[TransitionEvent]]:
    """
    Creates a specification for a TransitionEvent.

    Args:
        ev (rx.Var[TransitionEvent]): The TransitionEvent variable.

    Returns:
        tuple[rx.Var[TransitionEvent]]: A tuple containing the TransitionEvent specification.
    """
    return (
        rx.Var.create(
            TransitionEvent(
                propertyName=ev.propertyName,
                elapsedTime=ev.elapsedTime,
                pseudoElement=ev.pseudoElement,
            )
        ),
    )


# WebGLContextEvent: https://developer.mozilla.org/en-US/docs/Web/API/WebGLContextEvent
@dataclasses.dataclass
class WebGLContextEvent:
    """
    Represents events related to the WebGL rendering context.

    Attributes:
        statusMessage (str): Status message describing the event
    """

    statusMessage: str = ""  # Status message describing the event


def webgl_context_event_spec(ev: rx.Var[WebGLContextEvent]) -> tuple[rx.Var[WebGLContextEvent]]:
    """
    Creates a specification for a WebGLContextEvent.

    Args:
        ev (rx.Var[WebGLContextEvent]): The WebGLContextEvent variable.

    Returns:
        tuple[rx.Var[WebGLContextEvent]]: A tuple containing the WebGLContextEvent specification.
    """
    return (rx.Var.create(WebGLContextEvent(statusMessage=ev.statusMessage)),)
