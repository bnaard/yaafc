from dataclasses import dataclass
from typing import TypeAlias

import reflex as rx


@dataclass
class Slot:
    row: int
    col: int
    rowspan: int = 1
    colspan: int = 1


Slots: TypeAlias = list[Slot]


class SlottedPageState(rx.ComponentState):
    slots: Slots = []  # noqa: RUF012
