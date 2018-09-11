_default_graph = None

def set_default(obj):
    global _default_graph
    _default_graph = obj

def get_default():
    global _default_graph
    return _default_graph
