"""
This file contains modular action functions for the GUI. Each function is intended to be
called by buttons or menus via the App instance, which holds all shared state 
(e.g., the current graph, figure, data, and UI update functions).

HOW TO USE / EXTEND:

1. Each function receives the `app` object, and optionally other relevant arguments 
   (like `graph_types` for navigation).
2. Functions should update the relevant attributes in `app` and then call 
   `app.update_frame()` to redraw the GUI and synchronize the UI.
3. To add new behaviors (e.g., toggling different overlays or settings):
   - Add a new function here following the same pattern.
   - Add a corresponding button/menu item in `App.create_gui()` linking to the new function.

CURRENT FUNCTIONS:

- next_graph(app, graph_types): Move to the next graph in the list.
- prev_graph(app, graph_types): Move to the previous graph in the list.
- toggle_avg(app): Toggle the average line display for graphs that support it.
"""

def next_graph(app, graph_types):
   """Move to the next graph in the list."""
   app.current_graph_index = (app.current_graph_index + 1) % len(graph_types)
   app.update_frame()

def prev_graph(app, graph_types):
   """Move to the previous graph in the list."""
   app.current_graph_index = (app.current_graph_index - 1) % len(graph_types)
   app.update_frame()

def toggle_avg(app):
   """Toggle the average line display for graphs that support it."""
   if hasattr(app, "data") and hasattr(app.data, "avg"):
      app.data.avg = not app.data.avg
      app.update_frame()