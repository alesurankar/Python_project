from tkinter import messagebox

# default placeholder function
def default(action):  
    messagebox.showinfo("Info", f"{action} (not implemented yet)")

# edit_menu functions
def undo(action):
    default(action)

def redo(action):
    default(action)

def cut(action):
    default(action)

def copy(action):
    default(action)

def paste(action):
    default(action)

def find(action):
    default(action)

def replace(action):
    default(action)

def find_in_files(action):
    default(action)

def replace_in_files(action):
    default(action)

def toggle_line_commands(action):
    default(action)

def toggle_block_comment(action):
    default(action)

def emmet_expand_abbreviation(action):
    default(action)
