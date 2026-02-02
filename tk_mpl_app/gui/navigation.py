import tkinter as tk
from gui.components.button import THEME, ModernButton


def make_navigation_buttons(root, buttons_info):
    top_frame = tk.Frame(root, bg=THEME["bg"])
    top_frame.pack(side="top", fill="x")

    buttons = {}

    for info in buttons_info:
        btn = ModernButton(
            top_frame,
            text=info["text"],
            command=info["command"],
            width=130,
            height=42,
            radius=20
        )
        btn.pack(side=info.get("side", "left"), padx=8)

        buttons[info["text"]] = btn

    return buttons


