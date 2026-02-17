import tkinter as tk
from othr.bar import Bar

class DropdownMenu:
    def __init__(self, btn, state, width=50, height=50):
        self.btn = btn
        self.state = state
        self.theme = state.theme
        self.root = btn.winfo_toplevel()
        self.visible = False
        # create bars
        self.outer, self.inner = self._create_inner_bar(btn, state, width, height)
        self.outer.place_forget()

    # ----------create dropdown_menu ----------
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

        return outer_bar, inner_bar


    # ---------- toggle visibility ----------
    def show(self):
        if not self.visible:
            x = self.btn.winfo_rootx() - self.root.winfo_rootx()
            y = self.btn.winfo_rooty() - self.root.winfo_rooty() + self.btn.winfo_height()
            self._place_coords = (x, y)

            self.outer.place(x=x, y=y)
            self.outer.lift()
            self.root.update_idletasks()
            self.visible = True

    def hide(self):
        if self.visible:
            self.outer.place_forget()
            self.visible = False

    def toggle(self):
        if self.visible:
            self.hide()
        else:
            self.show()


    # ---------- add command ----------
    def add_command(self, label, command=None, height=24, padding=4):
        theme = self.theme

        label = tk.Label(
            self.inner.canvas,
            text=label,
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
    
    # ---------- add seperator ----------
    def add_separator(self, height=1, padding=4, color=None):
        """Add a horizontal separator line."""
        color = color or self.theme.get("menu_bar_bg") 
        sep = tk.Frame(
            self.inner.canvas,
            bg=color,
            height=height,
            bd=0
        )

        sep_id = self.inner.canvas.create_window(
        (0, self.inner._current_y + padding // 2),
            window=sep,
            anchor="nw",
            width=self.inner.winfo_width() 
        )

        def update_width():
            self.inner.canvas.itemconfig(sep_id, width=self.inner.winfo_width())
        self.inner.after(1, update_width)

        self.inner._current_y += height + padding
        return sep

