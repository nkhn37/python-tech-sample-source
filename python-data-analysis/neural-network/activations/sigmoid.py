"""ニューラルネットワークの活性化関数
シグモイド(sigmoid)関数

[説明ページ]
https://tech.nkhn37.net/neural-network-activations/#sigmoid
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-whitegrid")


def sigmoid(x):
    """シグモイド関数

    Args:
        x: 入力

    Returns:
        出力
    """
    return 1 / (1 + np.exp(-x))


def main():
    """メイン関数"""
    
    x = np.arange(-10, 10, 0.1)
    y = sigmoid(x)

    # グラフの描画
    plt.plot(x, y, label="sigmoid(x)")
    plt.title("sigmoid function")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
