from tkinter import ttk


def make_navigation_buttons(root, buttons_info):
    style_it_now()
    
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

def style_it_now():
    # Option 1: to style with ttk    (easy)
    # Option2: to style with Canvas  (better)
    
    style = ttk.Style()
    style.theme_use('clam')
    #themes ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')

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
        background=[("active", "#FF5733")],
        foreground=[("disabled", "#888888")],
        relief=[("pressed", "sunken")]
    )