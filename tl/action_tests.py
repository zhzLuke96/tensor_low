from tansor import Graph, Variable, placeholder, Session
from tansor.Activation import sigmoid, softmax


if __name__ == '__main__':
    from base_tests import add, matmul
    # 创建一个新 graph
    Graph().as_default()

    x = placeholder()
    w = Variable([1, 1])
    b = Variable(0)
    p = sigmoid(add(matmul(w, x), b))

    session = Session()
    print(session.run(p, {
        x: [3, 2]
    }))

    # softmax
    # 创建一些集中于 (-2, -2) 的红点
    red_points = np.random.randn(50, 2) - 2*np.ones((50, 2))

    # 创建一些集中于 (2, 2) 的蓝点
    blue_points = np.random.randn(50, 2) + 2*np.ones((50, 2))

    # 创建一个新 graph
    Graph().as_default()

    X = placeholder()

    # 为两种输出类别创建一个权矩阵:
    # 蓝色的权向量是 (1, 1) ，红色是 (-1, -1)
    W = Variable([
        [1, -1],
        [1, -1]
    ])
    b = Variable([0, 0])
    p = softmax( add(matmul(X, W), b) )

    # 创建一个 Session，针对我们的蓝色/红色点运行 perceptron
    session = Session()
    output_probabilities = session.run(p, {
        X: np.concatenate((blue_points, red_points))
    })

    # 打印前 10 行, 也就是前 10 个点的概率
    # print(output_probabilities[:10])
    print(output_probabilities)
