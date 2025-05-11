import reflex as rx

from yaafc.events.animation_transition_events import (
    animation_end_event_spec,
    animation_iteration_event_spec,
    animation_start_event_spec,
    transition_event_spec,
    webgl_context_event_spec,
)
from yaafc.events.clipboard_events import (
    copy_event_spec,
    cut_event_spec,
    paste_event_spec,
)
from yaafc.events.custom_events import custom_event_spec
from yaafc.events.fetch_form_submit_events import submit_event_spec
from yaafc.events.focus_events import (
    blur_event_spec,
    focus_event_spec,
    focus_in_event_spec,
)
from yaafc.events.gamepad_hash_popstate_storage_events import (
    hash_change_event_spec,
    pop_state_event_spec,
    storage_event_spec,
)
from yaafc.events.generic_events import progress_event_spec, security_policy_violation_event_spec
from yaafc.events.keyboard_events import (
    before_input_event_spec,
    composition_end_event_spec,
    composition_start_event_spec,
    composition_update_event_spec,
    input_event_spec,
    key_down_event_spec,
    key_up_event_spec,
)
from yaafc.events.mouse_events import (
    double_click_event_spec,
    drag_end_event_spec,
    drag_enter_event_spec,
    drag_event_spec,
    drag_leave_event_spec,
    drag_over_event_spec,
    drag_start_event_spec,
    drop_event_spec,
    mouse_event_spec,
    wheel_event_spec,
)
from yaafc.events.pointer_events import (
    got_pointer_capture_event_spec,
    lost_pointer_capture_event_spec,
    pointer_cancel_event_spec,
    pointer_down_event_spec,
    pointer_enter_event_spec,
    pointer_leave_event_spec,
    pointer_move_event_spec,
    pointer_out_event_spec,
    pointer_over_event_spec,
    pointer_up_event_spec,
)
from yaafc.events.touch_events import touch_event_spec
from yaafc.events.ui_events import (
    scroll_end_event_spec,
    scroll_event_spec,
)
from yaafc.events.unload_transition_events import (
    before_unload_event_spec,
    page_transition_event_spec,
)


class EnhancedEventWatcher(rx.el.Div):
    # Mouse events
    on_mouse_down: rx.EventHandler[mouse_event_spec]
    on_mouse_up: rx.EventHandler[mouse_event_spec]
    on_mouse_move: rx.EventHandler[mouse_event_spec]
    on_mouse_enter: rx.EventHandler[mouse_event_spec]
    on_mouse_leave: rx.EventHandler[mouse_event_spec]
    on_click: rx.EventHandler[mouse_event_spec]
    on_double_click: rx.EventHandler[double_click_event_spec]
    on_wheel: rx.EventHandler[wheel_event_spec]
    # Pointer events
    on_pointer_down: rx.EventHandler[pointer_down_event_spec]
    on_pointer_up: rx.EventHandler[pointer_up_event_spec]
    on_pointer_move: rx.EventHandler[pointer_move_event_spec]
    on_pointer_enter: rx.EventHandler[pointer_enter_event_spec]
    on_pointer_leave: rx.EventHandler[pointer_leave_event_spec]
    on_pointer_over: rx.EventHandler[pointer_over_event_spec]
    on_pointer_out: rx.EventHandler[pointer_out_event_spec]
    on_got_pointer_capture: rx.EventHandler[got_pointer_capture_event_spec]
    on_lost_pointer_capture: rx.EventHandler[lost_pointer_capture_event_spec]
    on_pointer_cancel: rx.EventHandler[pointer_cancel_event_spec]
    # Keyboard events
    on_key_down: rx.EventHandler[key_down_event_spec]
    on_key_up: rx.EventHandler[key_up_event_spec]
    # Touch events
    on_touch_start: rx.EventHandler[touch_event_spec]
    on_touch_end: rx.EventHandler[touch_event_spec]
    on_touch_move: rx.EventHandler[touch_event_spec]
    on_touch_cancel: rx.EventHandler[touch_event_spec]
    # Focus events
    on_focus: rx.EventHandler[focus_event_spec]
    on_blur: rx.EventHandler[blur_event_spec]
    on_focus_in: rx.EventHandler[focus_in_event_spec]
    # Clipboard events
    on_copy: rx.EventHandler[copy_event_spec]
    on_cut: rx.EventHandler[cut_event_spec]
    on_paste: rx.EventHandler[paste_event_spec]
    # Drag & Drop events
    on_drag: rx.EventHandler[drag_event_spec]
    on_drag_start: rx.EventHandler[drag_start_event_spec]
    on_drag_end: rx.EventHandler[drag_end_event_spec]
    on_drag_enter: rx.EventHandler[drag_enter_event_spec]
    on_drag_leave: rx.EventHandler[drag_leave_event_spec]
    on_drag_over: rx.EventHandler[drag_over_event_spec]
    on_drop: rx.EventHandler[drop_event_spec]
    # UI events
    on_scroll: rx.EventHandler[scroll_event_spec]
    on_scroll_end: rx.EventHandler[scroll_end_event_spec]
    # Animation/Transition events
    on_animation_start: rx.EventHandler[animation_start_event_spec]
    on_animation_end: rx.EventHandler[animation_end_event_spec]
    on_animation_iteration: rx.EventHandler[animation_iteration_event_spec]
    on_transition_end: rx.EventHandler[transition_event_spec]
    # Custom events
    on_custom: rx.EventHandler[custom_event_spec]
    # Form events
    on_submit: rx.EventHandler[submit_event_spec]
    # Input events
    on_input: rx.EventHandler[input_event_spec]
    on_before_input: rx.EventHandler[before_input_event_spec]
    # Composition events
    on_composition_start: rx.EventHandler[composition_start_event_spec]
    on_composition_update: rx.EventHandler[composition_update_event_spec]
    on_composition_end: rx.EventHandler[composition_end_event_spec]
    # Generic events
    on_progress: rx.EventHandler[progress_event_spec]
    # Unload/Page transition events
    on_before_unload: rx.EventHandler[before_unload_event_spec]
    on_page_transition: rx.EventHandler[page_transition_event_spec]
    # Storage/Hash/Popstate events
    on_storage: rx.EventHandler[storage_event_spec]
    on_hash_change: rx.EventHandler[hash_change_event_spec]
    on_pop_state: rx.EventHandler[pop_state_event_spec]
    # WebGL context events
    on_webgl_context: rx.EventHandler[webgl_context_event_spec]
    # Security policy violation
    on_security_policy_violation: rx.EventHandler[security_policy_violation_event_spec]
