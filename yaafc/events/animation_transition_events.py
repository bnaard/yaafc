import dataclasses

import reflex as rx


# AnimationEvent: https://developer.mozilla.org/en-US/docs/Web/API/AnimationEvent
@dataclasses.dataclass
class AnimationEvent:
    """Represents events providing information about animations."""

    animationName: str = ""  # Name of the animation
    elapsedTime: float = 0.0  # Time the animation has been running (in seconds)
    pseudoElement: str = ""  # Pseudo-element the animation applies to


def animation_event_spec(ev: rx.Var[AnimationEvent]) -> tuple[rx.Var[AnimationEvent]]:
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
    """Represents an animationend event."""

    pass


def animation_end_event_spec(ev: rx.Var[AnimationEndEvent]) -> tuple[rx.Var[AnimationEndEvent]]:
    return (rx.Var.create(AnimationEndEvent(**dataclasses.asdict(animation_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class AnimationIterationEvent(AnimationEvent):
    """Represents an animationiteration event."""

    pass


def animation_iteration_event_spec(ev: rx.Var[AnimationIterationEvent]) -> tuple[rx.Var[AnimationIterationEvent]]:
    return (rx.Var.create(AnimationIterationEvent(**dataclasses.asdict(animation_event_spec(ev)[0].get()))),)


@dataclasses.dataclass
class AnimationStartEvent(AnimationEvent):
    """Represents an animationstart event."""

    pass


def animation_start_event_spec(ev: rx.Var[AnimationStartEvent]) -> tuple[rx.Var[AnimationStartEvent]]:
    return (rx.Var.create(AnimationStartEvent(**dataclasses.asdict(animation_event_spec(ev)[0].get()))),)


# TransitionEvent: https://developer.mozilla.org/en-US/docs/Web/API/TransitionEvent
@dataclasses.dataclass
class TransitionEvent:
    """Represents events providing information about CSS transitions."""

    propertyName: str = ""  # Name of the CSS property transitioning
    elapsedTime: float = 0.0  # Time the transition has been running (in seconds)
    pseudoElement: str = ""  # Pseudo-element the transition applies to


def transition_event_spec(ev: rx.Var[TransitionEvent]) -> tuple[rx.Var[TransitionEvent]]:
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
    """Represents events related to the WebGL rendering context."""

    statusMessage: str = ""  # Status message describing the event


def webgl_context_event_spec(ev: rx.Var[WebGLContextEvent]) -> tuple[rx.Var[WebGLContextEvent]]:
    return (rx.Var.create(WebGLContextEvent(statusMessage=ev.statusMessage)),)
