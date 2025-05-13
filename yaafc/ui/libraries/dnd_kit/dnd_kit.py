import reflex as rx


class DndContext(rx.Component):
    library = "@dnd-kit/core"
    tag = "DndContext"
    is_default = True


class DragOverlay(rx.Component):
    library = "@dnd-kit/core"
    tag = "DragOverlay"


class UseDraggable(rx.Component):
    library = "@dnd-kit/core"
    tag = "useDraggable"
    is_hook = True


class UseDroppable(rx.Component):
    library = "@dnd-kit/core"
    tag = "useDroppable"
    is_hook = True


class CSS(rx.Component):
    library = "@dnd-kit/utilities"
    tag = "CSS"
