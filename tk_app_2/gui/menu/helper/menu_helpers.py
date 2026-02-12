
def ensure_namespace(root, name):
    if not hasattr(root, name):
        setattr(root, name, type(name, (), {})())
    return getattr(root, name)
