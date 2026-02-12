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

        # Top buttons
        top_frame = tk.Frame(c, bg=self.theme.get("activity_bar_bg"))
        c.create_window((0, 0), window=top_frame, anchor="nw")
        for icon, name in [
                ("📁", "Explorer"),
                ("🔍", "Search"),
                ("🧩", "Source Control"),
                ("▶️", "Run"),
                ("🔌", "Extensions"),
                ("🧪", "Testing")
            ]:
            self._add_button(icon, name, top_frame)

        # Bottom buttons
        bottom_frame = tk.Frame(c, bg=self.theme.get("activity_bar_bg"))
        bottom_frame.pack(side="bottom", fill="x")
        for icon, name in [
                ("👤", "Accounts"), 
                ("⚙️", "Settings")
            ]:
            self._add_button(icon, name, bottom_frame, is_menu=True)

        top_frame.update_idletasks()
        c.config(scrollregion=c.bbox("all"))


    def _add_button(self, icon, name, parent, is_menu=False):
        btn = tk.Label(
            parent,
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
        btn.tooltip = name 

        # hover effect
        btn.bind("<Enter>", lambda e: btn.config(fg=self.theme.get("activity_bar_text_hover")))
        btn.bind("<Leave>", lambda e: self._deactivate(btn))
        if is_menu:
            btn.bind("<Button-1>", lambda e: self._toggle_menu(btn))
        else:
            btn.bind("<Button-1>", lambda e: self._activate(btn))


    def _set_default_active(self):
        explorer_btn = self.buttons.get("Explorer")
        if self.state.show_primary_side_bar.get() and explorer_btn:
            self._activate(explorer_btn)

    def _activate(self, btn):
        # Top buttons (primary side bar)
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


    def _toggle_menu(self, btn):
        # if menu already open, close it
        if getattr(btn, "_menu_open", False):
            btn._menu.unpost()
            btn._menu_open = False
            btn.config(fg=self.theme.get("activity_bar_text"))
            return
        
        # create menu
        menu = tk.Menu(self, tearoff=0, bg=self.theme.get("activity_bar_bg"),
                       fg=self.theme.get("activity_bar_text"))
        if btn.tooltip == "Accounts":
            menu.add_command(label="Sign In", command=lambda: print("Sign In clicked"))
            menu.add_command(label="Manage Accounts", command=lambda: print("Manage Accounts clicked"))
        else:  # Settings
            menu.add_command(label="Settings", command=lambda: print("Settings clicked"))
            menu.add_command(label="Keyboard Shortcuts", command=lambda: print("Keyboard Shortcuts clicked"))
            menu.add_command(label="Themes", command=lambda: print("Color Theme clicked"))

        # show menu
        x, y = btn.winfo_rootx() + btn.winfo_width(), btn.winfo_rooty()
        menu.tk_popup(x, y)
        btn._menu = menu
        btn._menu_open = True

        # close menu if clicking outside
        def close_menu(event):
            # ignore clicks inside the button or menu
            if event.widget in (btn, menu):
                return
            if btn._menu_open:
                menu.unpost()
                btn._menu_open = False
                btn.config(fg=self.theme.get("activity_bar_text"))
            # remove the binding after closing
            self.unbind_all("<Button-1>")

        self.bind_all("<Button-1>", close_menu, add="+")
        menu.bind("<Unmap>", lambda e: self.unbind_all("<Button-1>"))