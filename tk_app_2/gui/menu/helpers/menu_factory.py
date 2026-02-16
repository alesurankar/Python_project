import tkinter as tk


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