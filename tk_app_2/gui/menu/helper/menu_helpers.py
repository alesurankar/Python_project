from tkinter import messagebox
import inspect


def ensure_namespace(root, name):
    if not hasattr(root, name):
        setattr(root, name, type(name, (), {})())
    return getattr(root, name)


def cmd(action, module):
    return lambda: dispatch(action, module)


def dispatch(action, module=None):
    if module is None:
        messagebox.showinfo("Error", f"No module provided for '{action}'")
        print("❌ Missing module for:", action)
        return

    func = getattr(module, action, None)
    if not callable(func):
        messagebox.showinfo("Info", f"Function '{action}' does not exist in {module.__name__}")
        print("❌ Missing function:", action)
        return

    try:
        sig = inspect.signature(func)
        if len(sig.parameters) == 0:
            func()
        else:
            func(action)
    except Exception as e:
        messagebox.showinfo("Error", f"Error calling '{action}': {e}")
        print("❌ Exception in function:", action, e)
