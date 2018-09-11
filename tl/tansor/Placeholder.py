# from .Graph import _default_graph
from .globals import get_default


__all__ = ("placeholder",)

class placeholder:
    """Represents a placeholder node that has to be provided with a value
       when computing the output of a computational graph
    """

    def __init__(self):
        """Construct placeholder
        """
        # global _default_graph
        self.consumers = []

        # Append this placeholder to the list of placeholders in the currently active default graph
        get_default().placeholders.append(self)
