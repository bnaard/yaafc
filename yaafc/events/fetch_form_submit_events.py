"""
Fetch, form, and submit event dataclasses and event spec functions for DOM event handling.

This module provides Python representations of fetch, form, and submit DOM events, including their event spec functions for use with Reflex event handlers.
"""

import dataclasses

import reflex as rx


@dataclasses.dataclass
class Request:
    """
    Represents a resource request.

    Attributes:
        method (str): HTTP method
        url (str): Request URL
        headers (dict): HTTP headers
        body (str): Request body (if any)
        mode (str): Request mode (e.g., 'cors', 'no-cors', 'same-origin')
        credentials (str): Request credentials ('omit', 'same-origin', 'include')
        cache (str): Cache mode
        redirect (str): Redirect mode
        referrer (str): Referrer URL
        referrerPolicy (str): Referrer policy
        integrity (str): Subresource integrity value
        keepalive (bool): Keepalive flag
        signal (str): AbortSignal (as string or id)
        destination (str): Request destination
        isReloadNavigation (bool): True if reload navigation
        isHistoryNavigation (bool): True if history navigation
    """

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


@dataclasses.dataclass
class FetchEvent:
    """
    Represents events that are fired when a fetch request is made in a service worker.

    Attributes:
        request (Request): The Request object
        clientId (str): The ID of the client that initiated the fetch
        isReload (bool): True if the request is a reload
    """

    request: Request = dataclasses.field(default_factory=Request)  # The Request object
    clientId: str = ""  # The ID of the client that initiated the fetch
    isReload: bool = False  # True if the request is a reload


def fetch_event_spec(ev: rx.Var[FetchEvent]) -> tuple[rx.Var[FetchEvent]]:
    """
    Creates a fetch event specification.

    Args:
        ev (rx.Var[FetchEvent]): The fetch event variable.

    Returns:
        tuple[rx.Var[FetchEvent]]: A tuple containing the fetch event variable.
    """
    return (
        rx.Var.create(
            FetchEvent(
                request=ev.request,
                clientId=ev.clientId,
                isReload=ev.isReload,
            )
        ),
    )


@dataclasses.dataclass
class FormData:
    """
    Represents a set of key/value pairs sent using XMLHttpRequest or Fetch.

    Attributes:
        entries (dict): Form data as key/value pairs
    """

    entries: dict = dataclasses.field(default_factory=dict)  # Form data as key/value pairs


@dataclasses.dataclass
class FormDataEvent:
    """
    Represents events that are fired when a form is submitted and the entry list is constructed.

    Attributes:
        formData (FormData): The FormData object
    """

    formData: FormData = dataclasses.field(default_factory=FormData)  # The FormData object


def form_data_event_spec(ev: rx.Var[FormDataEvent]) -> tuple[rx.Var[FormDataEvent]]:
    """
    Creates a form data event specification.

    Args:
        ev (rx.Var[FormDataEvent]): The form data event variable.

    Returns:
        tuple[rx.Var[FormDataEvent]]: A tuple containing the form data event variable.
    """
    return (rx.Var.create(FormDataEvent(formData=ev.formData)),)


@dataclasses.dataclass
class SubmitEvent:
    """
    Represents events that are fired when a form is submitted.

    Attributes:
        submitter (str): The element that was used to submit the form (serialized as string)
    """

    submitter: str = ""  # The element that was used to submit the form (serialized as string)


def submit_event_spec(ev: rx.Var[SubmitEvent]) -> tuple[rx.Var[SubmitEvent]]:
    """
    Creates a submit event specification.

    Args:
        ev (rx.Var[SubmitEvent]): The submit event variable.

    Returns:
        tuple[rx.Var[SubmitEvent]]: A tuple containing the submit event variable.
    """
    return (rx.Var.create(SubmitEvent(submitter=ev.submitter)),)
