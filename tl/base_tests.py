from tensor import Graph, Variable, Operation, placeholder, Session, get_default

__all__ = ("add", "matmul")


class add(Operation):
    """Returns x + y element-wise.
    """

    def __init__(self, x, y):
        """Construct add

        Args:
          x: First summand node
          y: Second summand node
        """
        super().__init__([x, y])

    def compute(self, x_value, y_value):
        """Compute the output of the add operation

        Args:
          x_value: First summand value
          y_value: Second summand value
        """
        return x_value + y_value


class matmul(Operation):
    """Multiplies matrix a by matrix b, producing a * b.
    """

    def __init__(self, a, b):
        """Construct matmul

        Args:
          a: First matrix
          b: Second matrix
        """
        super().__init__([a, b])

    def compute(self, a_value, b_value):
        """Compute the output of the matmul operation

        Args:
          a_value: First matrix value
          b_value: Second matrix value
        """
        return a_value.dot(b_value)


if __name__ == '__main__':
    # Create a new graph
    Graph().as_default()
    # graph_init()

    print(get_default())

    # Create variables
    A = Variable([[1, 0], [0, -1]])
    b = Variable([1, 1])

    # Create placeholder
    x = placeholder()

    # Create hidden node y
    y = matmul(A, x)

    # Create output node z
    z = add(y, b)

    session = Session()
    output = session.run(z, {
        x: [1, 2]
    })
    print(output)
