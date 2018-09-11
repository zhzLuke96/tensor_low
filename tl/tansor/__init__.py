from .Graph import Graph
from .Operation import Operation
from .Placeholder import placeholder
from .Variable import Variable
from .Session import Session
from .globals import set_default, get_default


def graph_init():
    Graph().as_default()
