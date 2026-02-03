from dataclasses import dataclass


@dataclass
class AppState:
    counter: int = 0
    active_widget: str = ""
    show_menu: bool = True
    show_nav: bool = True
    show_graph: bool = True
    show_game: bool = True