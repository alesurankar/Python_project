from gui.menu.commands import selection_cmd
from gui.menu.helpers import menu_helpers as helper
from gui.menu.helpers.dropdown_menu import DropdownMenu


def create_selection_menu(btn, state):
    btn.menu = DropdownMenu(btn, state, width=220, height=464)
    btn.menu.add_command(label="Select All", command=helper.cmd("select_all", selection_cmd))
    btn.menu.add_command(label="Expand Selection", command=helper.cmd("expand_selection", selection_cmd))
    btn.menu.add_command(label="Shrink Selection", command=helper.cmd("shrink_selection", selection_cmd))
    btn.menu.add_separator()

    btn.menu.add_command(label="Copy Line Up", command=helper.cmd("copy_line_up", selection_cmd))
    btn.menu.add_command(label="Copy Line Down", command=helper.cmd("copy_line_down", selection_cmd))
    btn.menu.add_command(label="Move Line Up", command=helper.cmd("move_line_up", selection_cmd))
    btn.menu.add_command(label="Move Line Down", command=helper.cmd("move_line_down", selection_cmd))
    btn.menu.add_command(label="Duplicate Selection", command=helper.cmd("duplicate_selection", selection_cmd))
    btn.menu.add_separator()

    btn.menu.add_command(label="Add Cursor Above", command=helper.cmd("add_cursor_above", selection_cmd))
    btn.menu.add_command(label="Add Cursor Below", command=helper.cmd("add_cursor_below", selection_cmd))
    btn.menu.add_command(label="Add Cursors to Line Ends", command=helper.cmd("add_cursor_to_line_ends", selection_cmd))
    btn.menu.add_command(label="Add Next Occurrence", command=helper.cmd("add_next_occurrence", selection_cmd))
    btn.menu.add_command(label="Add Previous Occurrence", command=helper.cmd("add_previous_occurrence", selection_cmd))
    btn.menu.add_command(label="Select All Occurrences", command=helper.cmd("select_all_occurrences", selection_cmd))
    btn.menu.add_separator()

    btn.menu.add_command(label="Switch to Ctrl+Click for Multi-Cursor", command=helper.cmd("switch_to_ctrl_and_click_for_multi_cursor", selection_cmd))
    btn.menu.add_command(label="Column Selection Mode", command=helper.cmd("column_selection_mode", selection_cmd))

def expand_selection_menu(btn):
    btn.menu.show()

def colapse_selection_menu(btn):
    btn.menu.hide()