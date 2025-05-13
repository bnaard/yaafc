# YAAFC Yet Another Absurd FileCommander - Layout Page Tasks

## Current Tasks

- [x] In the layout() function, extract the first rx.card component into a separate CompnentState based class. Name this new class "WidgetStack". Extract the new class into a separate file in the yaafc/ui/widgets directory.
- [x] Add a new method to this class called "registerWidget" that allows to register an rx.Component to the class with a name and the create function of that widget.
- [x] In the WidgetStack class, add the possibility not only to register a widget name and create-function, but also register a widget description and an icon.
- [x] Add to the registration function the possibility to specify also a widgets size in grid_columns and grid_rows.
- [x] Create a new class method that provides an rx.component that can represent a widget registered in the WidgetStack class, eg by having the icon at the left, and at the right a headline with the widget's name and below the description.
- [x] Create a new class method that provides a list of all the registered widgets using the representation-compnent created in the previous step. make sure you use the reflex way of iterating over list by using rx.foreach.
- [x] Use the method to provide a list of all registered widgets in the layout() function.
- [x] In WidgetStack class, make the component produced by the widget_repr_component method to be draggable.
- [ ] The draggable component should be able to be dropped into a grid layout.
- [ ] The grid layout should be able to accept the dropped component and place it in the grid.

## Discovered During Work
