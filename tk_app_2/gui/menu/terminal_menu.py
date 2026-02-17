from gui.menu.commands import terminal_cmd
from gui.menu.helpers import menu_helpers as helper
from gui.menu.helpers.dropdown_menu import DropdownMenu


def create_terminal_menu(btn, state):
    btn.menu = DropdownMenu(btn, state, width=190, height=352)
    btn.menu.add_command(label="New Terminal", command=helper.cmd("new_terminal", terminal_cmd))
    btn.menu.add_command(label="Split Terminal", command=helper.cmd("split_terminal", terminal_cmd))
    btn.menu.add_command(label="New Terminal Window", command=helper.cmd("new_terminal_window", terminal_cmd))
    btn.menu.add_separator()
    
    btn.menu.add_command(label="Run Task...", command=helper.cmd("run_task", terminal_cmd))
    btn.menu.add_command(label="Run Build Task...", command=helper.cmd("run_build_task", terminal_cmd))
    btn.menu.add_command(label="Run Active File...", command=helper.cmd("run_active_file", terminal_cmd))
    btn.menu.add_command(label="Run Selected Text...", command=helper.cmd("run_selected_text", terminal_cmd))
    btn.menu.add_separator()
    
    btn.menu.add_command(label="Show Running Tasks...", command=helper.cmd("show_running_tasks", terminal_cmd))
    btn.menu.add_command(label="Restart Running Task...", command=helper.cmd("restart_running_task", terminal_cmd))
    btn.menu.add_command(label="Terminate Task...", command=helper.cmd("terminate_task", terminal_cmd))
    btn.menu.add_separator()
    
    btn.menu.add_command(label="Configure Tasks...", command=helper.cmd("configure_tasks", terminal_cmd))
    btn.menu.add_command(label="Configure Default Build Task...", command=helper.cmd("configure_default_build_task", terminal_cmd))

def expand_terminal_menu(btn):
    btn.menu.show()

def colapse_terminal_menu(btn):
    btn.menu.hide()