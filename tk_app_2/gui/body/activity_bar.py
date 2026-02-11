import tkinter as tk
from othr.bar import Bar


class ActivityBar(tk.Frame):
    def __init__(self, root, state, layout=None):
        super().__init__(root)
        self.state = state
        self.layout = layout
        self.theme = state.theme
        self.active_btn = None
        self.buttons = {}
        
        self.activity_bar = Bar(self, self.state, 50, 0, self.theme.get("activity_bar_bg"))
        self.activity_bar.pack(side="left", fill="y")

        self._build_ui()
        self._set_default_active()
    
    def _build_ui(self):
        c = self.activity_bar.canvas

        self.btn_frame = tk.Frame(c, bg=self.theme.get("activity_bar_bg"))
        c.create_window((0, 0), window=self.btn_frame, anchor="nw")

        buttons = [
            ("📁", "Explorer"),
            ("🔍", "Search"),
            ("⚙️", "Settings"),
        ]

        for icon, name in buttons:
            self._add_button(icon, name)

        self.btn_frame.update_idletasks()
        c.config(scrollregion=c.bbox("all"))

    def _add_button(self, icon, name):
        btn = tk.Label(
            self.btn_frame,
            text=icon,
            font=("Segoe UI Emoji", 16),
            bg=self.theme.get("activity_bar_bg"),
            fg=self.theme.get("activity_bar_text"),
            padx=10,
            pady=8,
            cursor="hand2",
        )
        btn.pack(fill="x")
        self.buttons[name] = btn

        # hover effect
        btn.bind("<Enter>", lambda e: btn.config(fg=self.theme.get("activity_bar_text_hover")))
        btn.bind("<Leave>", lambda e: self._deactivate(btn))
        btn.bind("<Button-1>", lambda e: self._activate(btn))

        btn.tooltip = name 

    def _set_default_active(self):
        if self.state.show_primary_side_bar.get():
            explorer_btn = self.buttons.get("Explorer")
            if explorer_btn:
                self._activate(explorer_btn)
        else:
            self.active_btn = None

    def _activate(self, btn):
        if self.active_btn == btn:
            # If clicking the active button, deactivate it
            if self.layout.state.show_primary_side_bar.get():
                self.layout.hide_expand()
            else:
                self.layout.show_expand()
            self.active_btn = None
            btn.config(fg=self.theme.get("activity_bar_text"), bg=self.theme.get("activity_bar_bg"))
            return

        # Deactivate previous active button
        if self.active_btn:
            self.active_btn.config(fg=self.theme.get("activity_bar_text"), bg=self.theme.get("activity_bar_bg"))

        # Activate this one
        btn.config(fg=self.theme.get("activity_bar_text_hover"), bg=self.theme.get("primary_side_bar_bg"))
        self.active_btn = btn
        self.layout.show_expand()

    def _deactivate(self, btn):
        if btn != self.active_btn:
            btn.config(fg=self.theme.get("activity_bar_text"))