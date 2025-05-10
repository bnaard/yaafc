import dataclasses

import reflex as rx


# Request: https://developer.mozilla.org/en-US/docs/Web/API/Request
@dataclasses.dataclass
class Request:
    """Represents a resource request."""

    method: str = "GET"  # HTTP method
    url: str = ""  # Request URL
    headers: dict = dataclasses.field(default_factory=dict)  # HTTP headers
    body: str = ""  # Request body (if any)
    mode: str = ""  # Request mode (e.g., 'cors', 'no-cors', 'same-origin')
    credentials: str = ""  # Request credentials ('omit', 'same-origin', 'include')
    cache: str = ""  # Cache mode
    redirect: str = ""  # Redirect mode
    referrer: str = ""  # Referrer URL
    referrerPolicy: str = ""  # Referrer policy
    integrity: str = ""  # Subresource integrity value
    keepalive: bool = False  # Keepalive flag
    signal: str = ""  # AbortSignal (as string or id)
    destination: str = ""  # Request destination
    isReloadNavigation: bool = False  # True if reload navigation
    isHistoryNavigation: bool = False  # True if history navigation


# FetchEvent: https://developer.mozilla.org/en-US/docs/Web/API/FetchEvent
@dataclasses.dataclass
class FetchEvent:
    """Represents events that are fired when a fetch request is made in a service worker."""

    request: Request = dataclasses.field(default_factory=Request)  # The Request object
    clientId: str = ""  # The ID of the client that initiated the fetch
    isReload: bool = False  # True if the request is a reload


def fetch_event_spec(ev: rx.Var[FetchEvent]) -> tuple[rx.Var[FetchEvent]]:
    return (
        rx.Var.create(
            FetchEvent(
                request=ev.request,
                clientId=ev.clientId,
                isReload=ev.isReload,
            )
        ),
    )


# FormData: https://developer.mozilla.org/en-US/docs/Web/API/FormData
@dataclasses.dataclass
class FormData:
    """Represents a set of key/value pairs sent using XMLHttpRequest or Fetch."""

    entries: dict = dataclasses.field(default_factory=dict)  # Form data as key/value pairs


# FormDataEvent: https://developer.mozilla.org/en-US/docs/Web/API/FormDataEvent
@dataclasses.dataclass
class FormDataEvent:
    """Represents events that are fired when a form is submitted and the entry list is constructed."""

    formData: FormData = dataclasses.field(default_factory=FormData)  # The FormData object


def form_data_event_spec(ev: rx.Var[FormDataEvent]) -> tuple[rx.Var[FormDataEvent]]:
    return (rx.Var.create(FormDataEvent(formData=ev.formData)),)


# SubmitEvent: https://developer.mozilla.org/en-US/docs/Web/API/SubmitEvent
@dataclasses.dataclass
class SubmitEvent:
    """Represents events that are fired when a form is submitted."""

    submitter: str = ""  # The element that was used to submit the form (serialized as string)


def submit_event_spec(ev: rx.Var[SubmitEvent]) -> tuple[rx.Var[SubmitEvent]]:
    return (rx.Var.create(SubmitEvent(submitter=ev.submitter)),)
