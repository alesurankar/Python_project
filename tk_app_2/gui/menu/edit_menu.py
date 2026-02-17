from gui.menu.commands import edit_cmd
from gui.menu.helpers import menu_helpers as helper
from gui.menu.helpers.dropdown_menu import DropdownMenu


def create_edit_menu(btn, state):
    btn.menu = DropdownMenu(btn, state, width=180, height=357)
    btn.menu.add_command(label="Undo", command=helper.cmd("undo", edit_cmd))
    btn.menu.add_command(label="Redo", command=helper.cmd("redo", edit_cmd))
    btn.menu.add_separator()

    btn.menu.add_command(label="Cut", command=helper.cmd("cut", edit_cmd))
    btn.menu.add_command(label="Copy", command=helper.cmd("copy", edit_cmd))
    btn.menu.add_command(label="Paste", command=helper.cmd("paste", edit_cmd))
    btn.menu.add_separator()

    btn.menu.add_command(label="Find", command=helper.cmd("find", edit_cmd))
    btn.menu.add_command(label="Replace", command=helper.cmd("replace", edit_cmd))
    btn.menu.add_separator()

    btn.menu.add_command(label="Find in Files", command=helper.cmd("find_in_files", edit_cmd))
    btn.menu.add_command(label="Replace in Files", command=helper.cmd("replace_in_files", edit_cmd))
    btn.menu.add_separator()
    
    btn.menu.add_command(label="Toggle Line Comment", command=helper.cmd("toggle_line_commands", edit_cmd))
    btn.menu.add_command(label="Toggle Block comment", command=helper.cmd("toggle_block_comment", edit_cmd))
    btn.menu.add_command(label="Emmet: Expand Abbreviation", command=helper.cmd("emmet_expand_abbreviation", edit_cmd))

def expand_edit_menu(btn):
    btn.menu.show()

def colapse_edit_menu(btn):
    btn.menu.hide()