"""ニューラルネットワークの活性化関数
ReLU(Rectified Linear Unit)関数

[説明ページ]
https://tech.nkhn37.net/neural-network-activations/#ReLU
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-whitegrid")


def relu(x):
    """ReLU関数

    Args:
        x: 入力

    Returns:
        出力
    """
    return np.maximum(0, x)


def main():
    """メイン関数"""

    x = np.arange(-10, 10, 0.1)
    y = relu(x)

    # グラフの描画
    plt.plot(x, y, label="relu(x)")
    plt.title("relu function")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
