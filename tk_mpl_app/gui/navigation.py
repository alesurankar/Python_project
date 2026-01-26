import tkinter as ttk

def make_navigation_buttons(top_frame, show_next, show_prev):
    next_button = ttk.Button(top_frame, text="Next", command=show_next)
    next_button.pack(side="right", padx=5)
    prev_button = ttk.Button(top_frame, text="Previous", command=show_prev)
    prev_button.pack(side="right", padx=5)