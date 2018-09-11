from .globals import set_default

__all__ = ("Graph")

# _default_graph = None


class Graph:
    """Represents a computational graph
    """

    def __init__(self):
        """Construct Graph"""
        self.operations = []
        self.placeholders = []
        self.variables = []

    def as_default(self):
        set_default(self)
