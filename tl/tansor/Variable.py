# from .Graph import _default_graph
from .globals import get_default


__all__ = ("Variable",)

class Variable:
    """Represents a variable (i.e. an intrinsic, changeable parameter of a computational graph).
    """

    def __init__(self, initial_value=None):
        """Construct Variable

        Args:
          initial_value: The initial value of this variable
        """
        # global _default_graph
        self.value = initial_value
        self.consumers = []

        # Append this variable to the list of variables in the currently active default graph
        get_default().variables.append(self)
