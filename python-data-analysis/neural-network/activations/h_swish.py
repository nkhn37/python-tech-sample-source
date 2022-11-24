"""ニューラルネットワークの活性化関数
h-swish関数

[説明ページ]
https://tech.nkhn37.net/neural-network-activations/#h-swish
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


def h_swish(x):
    """h-swish関数

    Args:
        x: 入力

    Returns:
        出力
    """
    return x * relu6(x + 3) / 6


def main():
    """メイン関数"""
    
    x = np.arange(-10, 10, 0.1)
    y = h_swish(x)

    # グラフの描画
    plt.plot(x, y, label="h_swish(x)")
    plt.title("h-swish function")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
