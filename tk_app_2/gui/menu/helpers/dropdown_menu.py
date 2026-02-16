import tkinter as tk
from othr.bar import Bar

class DropdownMenu:
    def __init__(self, btn, state, width=120, height=200):
        self.btn = btn
        self.state = state
        self.theme = state.theme
        self.root = btn.winfo_toplevel()

        self.inner = self._create_inner_bar(btn, state, width, height)

        self.visible = False

    # ---------- wrap your create_dropdown_menu ----------
    def _create_inner_bar(self, btn, state, width, height):
        theme = state.theme
        root = btn.winfo_toplevel()

        outer_bar = Bar(
            root,
            state=state,
            width=width,
            height=height,
            border=0,
            bg_color=theme.get("menu_bar_bg")
        )

        inner_bar = Bar(
            outer_bar,
            state=state,
            width=width-2,
            height=height-2,
            border=0,
            bg_color=theme.get("menu_expand_bg")
        )
        inner_bar.place(x=1, y=1)
        inner_bar._current_y = 0

        x = btn.winfo_rootx() - root.winfo_rootx()
        y = btn.winfo_rooty() - root.winfo_rooty() + btn.winfo_height()
        outer_bar.place(x=x, y=y)

        self.outer = outer_bar
        return inner_bar

    # ---------- wrap your add_command ----------
    def add_command(self, text, command=None, height=24, padding=3):
        theme = self.theme

        label = tk.Label(
            self.inner.canvas,
            text=text,
            bg=theme.get("menu_expand_bg"),
            fg=theme.get("menu_expand_text"),
            anchor="w",
            padx=8,
            pady=4,
            cursor="hand2"
        )

        self.inner.canvas.create_window(
            (0, self.inner._current_y),
            window=label,
            anchor="nw",
            width=self.inner.winfo_reqwidth()
        )

        self.inner._current_y += height + padding

        if command:
            label.bind("<Button-1>", lambda e: (command(), self.hide()))

        def on_enter(e):
            label.config(
                bg=theme.get("menu_expand_bg_hover"),
                fg=theme.get("menu_expand_text_hover")
            )
        def on_leave(e):
            label.config(
                bg=theme.get("menu_expand_bg"),
                fg=theme.get("menu_expand_text")
            )

        label.bind("<Enter>", on_enter)
        label.bind("<Leave>", on_leave)

        return label

    # ---------- toggle visibility ----------
    def show(self):
        if not self.visible:
            self.outer.place()
            self.visible = True
            self.outer.lift()
            self.root.bind("<Button-1>", self._outside_click, add="+")

    def hide(self):
        if self.visible:
            self.outer.place_forget()
            self.visible = False
            self.root.unbind("<Button-1>")

    def toggle(self):
        if self.visible:
            self.hide()
        else:
            self.show()

    def _outside_click(self, event):
        widget = event.widget
        if widget is self.btn or self.outer.winfo_containing(event.x_root, event.y_root):
            return
        self.hide()
