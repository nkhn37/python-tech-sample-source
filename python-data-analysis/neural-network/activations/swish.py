"""ニューラルネットワークの活性化関数
swish関数

[説明ページ]
https://tech.nkhn37.net/neural-network-activations/#swish
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-whitegrid")


def sigmoid(x):
    """シグモイド関数
    :param x: 入力
    :return: 出力
    """
    return 1 / (1 + np.exp(-x))


def swish(x):
    """swish関数

    Args:
        x: 入力

    Returns:
        出力
    """
    return x * sigmoid(x)


def main():
    """メイン関数"""

    x = np.arange(-10, 10, 0.1)
    y = swish(x)

    # グラフの描画
    plt.plot(x, y, label="swish(x)")
    plt.title("swish function")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
