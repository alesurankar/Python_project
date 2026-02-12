import tkinter as tk


class AppState:
    def __init__(self, root):
        self.show_primary_side_bar = tk.BooleanVar(root, True)
        self.theme_name: str = "dark"
        self.themes: dict[str, dict[str, str]] = {
            "dark": {
                #menu
                "menu_bar_bg": "#3c3c3c",
                "menu_bar_text": "#b3b3b3",
                "menu_bar_bg_hover": "#454646",
                "menu_expand_bg": "#252526",
                "menu_expand_text": "#ffffff",
                "menu_expand_bg_hover": "#0078d4",
                #body
                "body_bg": "#1e1e1e",
                "body_text": "#ffffff",
                "activity_bar_bg": "#333333",
                "activity_bar_text": "#657885",
                "activity_bar_text_hover": "#ffffff",
                "primary_side_bar_bg": "#252526",
                #footer
                "footer_bg": "#007acc",
                "footer_text": "#ffffff",
            }
        }

    @property
    def theme(self):
        return self.themes[self.theme_name]