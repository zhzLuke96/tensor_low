from Operation import Operation
import numpy as np

__all__ = ("sigmoid","softmax")

class sigmoid(Operation):
    """返回元素 x 的 sigmoid 结果。
    """

    def __init__(self, a):
        """构造 sigmoid

        参数列表:
          a: 输入节点
        """
        super().__init__([a])

    def compute(self, a_value):
        """计算本 sigmoid operation 的输出

        参数列表:
          a_value: 输入值
        """
        return 1 / (1 + np.exp(-a_value))


class softmax(Operation):
    """返回 a 的 softmax 函数结果.
    """

    def __init__(self, a):
        """构造 softmax

        参数列表:
          a: 输入节点
        """
        super().__init__([a])

    def compute(self, a_value):
        """计算 softmax operation 的输出值

        参数列表:
          a_value: 输入值
        """
        return np.exp(a_value) / np.sum(np.exp(a_value), axis=1)[:, None]
