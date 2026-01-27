from tkinter import ttk


def make_navigation_buttons(root, buttons_info):
    style_it_out_of_its_ass()
    
    top_frame = ttk.Frame(root, padding=5, style="TopFrame.TFrame")
    top_frame.pack(side="top", fill="x")

    buttons = {}
    for info in buttons_info:
        btn = ttk.Button(
            top_frame, 
            text=info['text'], 
            command=info['command'], 
            style="Nav.TButton"
        )
        btn.pack(side=info.get('side', 'left'), padx=5)
        buttons[info['text']] = btn

        # Add real hover effect
        def on_enter(e, b=btn):
            b.configure(style="NavHover.TButton")
        def on_leave(e, b=btn):
            b.configure(style="Nav.TButton")
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    return buttons

def style_it_out_of_its_ass():
    style = ttk.Style()
    style.theme_use('clam') # Pick a good base theme

    # Top frame style
    style.configure("TopFrame.TFrame", background="#222222")

    # Navigation button style
    style.configure(
        "Nav.TButton",
        foreground="#ffffff",      # Text color
        background="#4CAF50",      # Base color
        font=("Helvetica", 11, "bold"),
        padding=(12, 6),           # x, y padding
        borderwidth=5,
        relief="raised"
    )

    # Hover button style (real)
    style.configure(
        "NavHover.TButton",
        foreground="#FFFF00",
        background="#FF5733",
        font=("Helvetica", 11, "bold"),
        padding=(12, 6),
        borderwidth=2,
        relief="raised"
    )

    # Pressed and disabled (optional)
    style.map(
        "Nav.TButton",
        relief=[("pressed", "sunken"), ("!pressed", "raised")],
        foreground=[("disabled", "#888888")],
        background=[("disabled", "#cccccc")]
    )

import tkinter as tk

def rounded_button(canvas, x, y, width, height, radius, text, command):
    tag = f"btn_{text}"
    # Draw shapes
    canvas.create_arc(x, y, x+2*radius, y+2*radius, start=90, extent=90, fill="#4CAF50", outline="#4CAF50", tags=tag)
    canvas.create_arc(x+width-2*radius, y, x+width, y+2*radius, start=0, extent=90, fill="#4CAF50", outline="#4CAF50", tags=tag)
    canvas.create_arc(x, y+height-2*radius, x+2*radius, y+height, start=180, extent=90, fill="#4CAF50", outline="#4CAF50", tags=tag)
    canvas.create_arc(x+width-2*radius, y+height-2*radius, x+width, y+height, start=270, extent=90, fill="#4CAF50", outline="#4CAF50", tags=tag)
    canvas.create_rectangle(x+radius, y, x+width-radius, y+height, fill="#4CAF50", outline="#4CAF50", tags=tag)
    canvas.create_rectangle(x, y+radius, x+width, y+height-radius, fill="#4CAF50", outline="#4CAF50", tags=tag)
    # Text
    canvas.create_text(x+width/2, y+height/2, text=text, fill="white", font=("Helvetica", 11, "bold"), tags=tag)
    # Bind click to the whole button
    canvas.tag_bind(tag, "<Button-1>", lambda e: command())

