import reflex as rx

from yaafc.events import (
    AnimationEvent,
    BeforeUnloadEvent,
    Blob,
    BlobEvent,
    ClipboardEvent,
    CloseEvent,
    CompositionEvent,
    CustomEvent,
    DragEndEvent,
    DragEnterEvent,
    DragEvent,
    DragLeaveEvent,
    DragOverEvent,
    DragStartEvent,
    DropEvent,
    Error,
    ErrorEvent,
    Event,
    FetchEvent,
    FocusEvent,
    FormData,
    FormDataEvent,
    Gamepad,
    GamepadEvent,
    HashChangeEvent,
    InputEvent,
    KeyboardEvent,
    MouseEvent,
    PageTransitionEvent,
    PointerEvent,
    PopStateEvent,
    ProgressEvent,
    Request,
    Storage,
    StorageEvent,
    SubmitEvent,
    TouchEvent,
    TransitionEvent,
    UIEvent,
    WebGLContextEvent,
    WheelEvent,
    animation_event_spec,
    before_unload_event_spec,
    blob_event_spec,
    clipboard_event_spec,
    close_event_spec,
    composition_event_spec,
    custom_event_spec,
    drag_end_event_spec,
    drag_enter_event_spec,
    drag_event_spec,
    drag_leave_event_spec,
    drag_over_event_spec,
    drag_start_event_spec,
    drop_event_spec,
    error_event_spec,
    event_spec,
    fetch_event_spec,
    focus_event_spec,
    form_data_event_spec,
    gamepad_event_spec,
    hash_change_event_spec,
    input_event_spec,
    keyboard_event_spec,
    mouse_event_spec,
    page_transition_event_spec,
    pointer_event_spec,
    pop_state_event_spec,
    progress_event_spec,
    storage_event_spec,
    submit_event_spec,
    touch_event_spec,
    transition_event_spec,
    ui_event_spec,
    webgl_context_event_spec,
    wheel_event_spec,
)


def test_gamepad_event():
    gamepad = Gamepad(
        id="g1", index=1, connected=True, mapping="standard", axes=[0.0, 1.0], buttons=[1, 0], timestamp=123.45
    )
    event = GamepadEvent(gamepad=gamepad)
    assert event.gamepad.id == "g1"
    assert event.gamepad.connected
    assert isinstance(gamepad_event_spec(rx.Var.create(event)), tuple)


def test_hash_change_event():
    event = HashChangeEvent(old_url="http://old", new_url="http://new")
    assert event.old_url == "http://old"
    assert event.new_url == "http://new"
    assert isinstance(hash_change_event_spec(rx.Var.create(event)), tuple)


def test_pop_state_event():
    event = PopStateEvent(state="some_state")
    assert event.state == "some_state"
    assert isinstance(pop_state_event_spec(rx.Var.create(event)), tuple)


def test_storage_event():
    storage = Storage(items={"foo": "bar"})
    event = StorageEvent(key="foo", old_value="bar", new_value="baz", url="http://test", storage_area=storage)
    assert event.storage_area.items["foo"] == "bar"
    assert isinstance(storage_event_spec(rx.Var.create(event)), tuple)


def test_mouse_event():
    event = MouseEvent(client_x=10, client_y=20, button=1)
    assert event.client_x == 10
    assert event.button == 1
    assert isinstance(mouse_event_spec(rx.Var.create(event)), tuple)


def test_wheel_event():
    event = WheelEvent(delta_x=1.0, delta_y=2.0, delta_z=0.0, delta_mode=1)
    assert event.delta_y == 2.0
    assert isinstance(wheel_event_spec(rx.Var.create(event)), tuple)


def test_pointer_event():
    event = PointerEvent(pointer_id=5, width=2.0, height=2.0, pressure=0.5)
    assert event.pointer_id == 5
    assert event.width == 2.0
    assert isinstance(pointer_event_spec(rx.Var.create(event)), tuple)


def test_drag_event():
    event = DragEvent(data_transfer="data")
    assert event.data_transfer == "data"
    assert isinstance(drag_event_spec(rx.Var.create(event)), tuple)


def test_drag_sub_events():
    for cls, spec in [
        (DragEnterEvent, drag_enter_event_spec),
        (DragLeaveEvent, drag_leave_event_spec),
        (DragOverEvent, drag_over_event_spec),
        (DragStartEvent, drag_start_event_spec),
        (DragEndEvent, drag_end_event_spec),
        (DropEvent, drop_event_spec),
    ]:
        event = cls(data_transfer="data")
        assert event.data_transfer == "data"
        assert isinstance(spec(rx.Var.create(event)), tuple)


def test_keyboard_event():
    event = KeyboardEvent(key="a", code="KeyA", ctrl_key=True)
    assert event.key == "a"
    assert event.ctrl_key
    assert isinstance(keyboard_event_spec(rx.Var.create(event)), tuple)


def test_input_event():
    event = InputEvent(data="x", input_type="insertText", is_composing=True)
    assert event.data == "x"
    assert event.is_composing
    assert isinstance(input_event_spec(rx.Var.create(event)), tuple)


def test_composition_event():
    event = CompositionEvent(data="ä")
    assert event.data == "ä"
    assert isinstance(composition_event_spec(rx.Var.create(event)), tuple)


def test_focus_event():
    event = FocusEvent(related_target="target")
    assert event.related_target == "target"
    assert isinstance(focus_event_spec(rx.Var.create(event)), tuple)


def test_ui_event():
    event = UIEvent(detail=2, view="window")
    assert event.detail == 2
    assert isinstance(ui_event_spec(rx.Var.create(event)), tuple)


def test_clipboard_event():
    event = ClipboardEvent(clipboard_data="copied")
    assert event.clipboard_data == "copied"
    assert isinstance(clipboard_event_spec(rx.Var.create(event)), tuple)


def test_custom_event():
    event = CustomEvent(detail="custom")
    assert event.detail == "custom"
    assert isinstance(custom_event_spec(rx.Var.create(event)), tuple)


def test_animation_event():
    event = AnimationEvent(animation_name="fade", elapsed_time=1.2, pseudo_element=":before")
    assert event.animation_name == "fade"
    assert isinstance(animation_event_spec(rx.Var.create(event)), tuple)


def test_transition_event():
    event = TransitionEvent(property_name="opacity", elapsed_time=0.5, pseudo_element=":after")
    assert event.property_name == "opacity"
    assert isinstance(transition_event_spec(rx.Var.create(event)), tuple)


def test_webgl_context_event():
    event = WebGLContextEvent(status_message="lost context")
    assert event.status_message == "lost context"
    assert isinstance(webgl_context_event_spec(rx.Var.create(event)), tuple)


def test_fetch_event():
    req = Request(method="POST", url="/api", headers={"Content-Type": "application/json"}, body="{}")
    event = FetchEvent(request=req, client_id="cid", is_reload=True)
    assert event.request.method == "POST"
    assert isinstance(fetch_event_spec(rx.Var.create(event)), tuple)


def test_form_data_event():
    form = FormData(entries={"foo": "bar"})
    event = FormDataEvent(form_data=form)
    assert event.form_data.entries["foo"] == "bar"
    assert isinstance(form_data_event_spec(rx.Var.create(event)), tuple)


def test_submit_event():
    event = SubmitEvent(submitter="button")
    assert event.submitter == "button"
    assert isinstance(submit_event_spec(rx.Var.create(event)), tuple)


def test_blob_event():
    blob = Blob(size=123, type="image/png")
    event = BlobEvent(data=blob, timecode=1.23)
    assert event.data.size == 123
    assert isinstance(blob_event_spec(rx.Var.create(event)), tuple)


def test_error_event():
    err = Error(name="TypeError", message="fail", stack="stacktrace")
    event = ErrorEvent(message="fail", filename="file.py", lineno=1, colno=2, error=err)
    assert event.error.name == "TypeError"
    assert isinstance(error_event_spec(rx.Var.create(event)), tuple)


def test_close_event():
    event = CloseEvent(was_clean=True, code=1000, reason="done")
    assert event.was_clean
    assert isinstance(close_event_spec(rx.Var.create(event)), tuple)


def test_touch_event():
    event = TouchEvent(alt_key=True, touches="[1,2]", target_touches="[1]", changed_touches="[2]")
    assert event.alt_key
    assert event.touches == "[1,2]"
    assert isinstance(touch_event_spec(rx.Var.create(event)), tuple)


def test_event_and_progress_event():
    event = Event(bubbles=True, type="test")
    assert event.bubbles
    assert isinstance(event_spec(rx.Var.create(event)), tuple)
    prog = ProgressEvent(length_computable=True, loaded=10, total=100)
    assert prog.length_computable
    assert isinstance(progress_event_spec(rx.Var.create(prog)), tuple)


def test_unload_and_page_transition_event():
    event = BeforeUnloadEvent(return_value="bye")
    assert event.return_value == "bye"
    assert isinstance(before_unload_event_spec(rx.Var.create(event)), tuple)
    page = PageTransitionEvent(persisted=True)
    assert page.persisted
    assert isinstance(page_transition_event_spec(rx.Var.create(page)), tuple)
