import tkinter as tk
from othr.bar import Bar


def create_menu_button(parent, text, theme, command=None):
    btn = tk.Label(
        parent,
        text=text,
        font=("Segoe UI Emoji", 10),
        bg=theme.get("menu_bar_bg"),
        fg=theme.get("menu_bar_text"),
        padx=4,
        pady=4,
    )
    btn.pack(side="left", padx=2)

    # hover effect
    def on_enter(e):
        btn.config(bg=theme.get("menu_bar_bg_hover"), fg=theme.get("menu_bar_text_hover"))

    def on_leave(e):
        btn.config(bg=theme.get("menu_bar_bg"), fg=theme.get("menu_bar_text"))

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    if command:
        btn.bind("<Button-1>", lambda e: command())

    return btn



def create_dropdown_menu(btn, state, width=120, height=200):
    theme = state.theme
    root = btn.winfo_toplevel()

    # Outer bar (border/background)
    outer_bar = Bar(root, state=state, width=width, height=height, border=0, bg_color=theme.get("menu_bar_bg"))

    # Inner bar (menu items container)
    inner_bar = Bar(outer_bar, state=state, width=width-2, height=height-2, border=0, bg_color=theme.get("menu_expand_bg"))
    inner_bar.place(x=1, y=1)

    # Track vertical offset for stacking items
    inner_bar._current_y = 0

    # Calculate absolute position relative to root
    x = btn.winfo_rootx() - root.winfo_rootx()
    y = btn.winfo_rooty() - root.winfo_rooty() + btn.winfo_height()
    outer_bar.place(x=x, y=y)

    return inner_bar


def add_command(inner_bar, state, text, height=24, padding=3, command=None):
    theme = state.theme

    label = tk.Label(
        inner_bar.canvas,
        text=text,
        bg=theme.get("menu_expand_bg"),
        fg=theme.get("menu_expand_text"),
        anchor="w",
        padx=8,
        pady=4,
        cursor="hand2"
    )

    inner_bar.canvas.create_window(
        (0, inner_bar._current_y),
        window=label,
        anchor="nw",
        width=inner_bar.winfo_reqwidth()
    )

    # Update vertical offset for next item
    inner_bar._current_y += height + padding

    if command:
        label.bind("<Button-1>", lambda e: command())

    # Hover effect
    def on_enter(e):
        label.config(bg=theme.get("menu_expand_bg_hover"), fg=theme.get("menu_expand_text_hover"))
    def on_leave(e):
        label.config(bg=theme.get("menu_expand_bg"), fg=theme.get("menu_expand_text"))

    label.bind("<Enter>", on_enter)
    label.bind("<Leave>", on_leave)

    return label