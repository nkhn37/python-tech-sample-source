"""ニューラルネットワークの活性化関数
Leaky ReLU関数

[説明ページ]
https://tech.nkhn37.net/neural-network-activations/#Leaky_ReLU
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-whitegrid")


def leaky_relu(x, alpha=0.1):
    """Leaky ReLU関数

    Args:
        x: 入力
        alpha: α値(デフォルト: 0.1)

    Returns:
        出力
    """
    return np.where(x >= 0, x, alpha * x)


def main():
    """メイン関数"""

    x = np.arange(-10, 10, 0.1)
    y = leaky_relu(x)

    # グラフの描画
    plt.plot(x, y, label="leaky_relu(x)")
    plt.title("leaky relu function")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
