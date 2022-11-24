"""ニューラルネットワークの活性化関数
ReLU6関数

[説明ページ]
https://tech.nkhn37.net/neural-network-activations/#ReLU6
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-whitegrid")


def relu6(x):
    """ReLU6関数

    Args:
        x: 入力

    Returns:
        出力
    """
    return np.minimum(np.maximum(0, x), 6)


def main():
    """メイン関数"""

    x = np.arange(-10, 10, 0.1)
    y = relu6(x)

    # グラフの描画
    plt.plot(x, y, label="relu6(x)")
    plt.title("relu6 function")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
