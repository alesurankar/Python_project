import tkinter as tk


class AppState:
    def __init__(self, root):
        self.show_primary_side_bar = tk.BooleanVar(root, True)
        self.theme_name: str = "dark"
        self.themes: dict[str, dict[str, str]] = {
            "dark": {
                "body_bg": "#1e1e1e",
                "body_text": "#ffffff",
                "activity_bar_bg": "#333333",
                "activity_bar_text": "#657885",
                "activity_bar_text_hover": "#ffffff",
                "primary_side_bar_bg": "#252526",
                "footer_bg": "#007acc",
                "footer_text": "white",
            }
        }

    @property
    def theme(self):
        return self.themes[self.theme_name]