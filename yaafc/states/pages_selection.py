import reflex as rx


class PagesSelectionState(rx.State):
    active_slot_ids: dict = {}  # noqa: RUF012

    def set_active_slot_id(self, page_id: str, slot_id: int):
        self.active_slot_ids[page_id] = slot_id
