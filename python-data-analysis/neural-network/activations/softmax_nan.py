"""ニューラルネットワークの活性化関数
softmax関数
実装上の注意点: オーバーフローによるnan

[説明ページ]
https://tech.nkhn37.net/neural-network-activations/#softmax-2
"""
import numpy as np


def softmax(x):
    """softmax関数

    Args:
        x: 入力

    Returns:
        出力
    """
    exp_x = np.exp(x)
    sum_exp = np.sum(exp_x)
    return exp_x / sum_exp


def main():
    """メイン関数"""

    x = np.array([1010, 1020, 1000, 990, 1050])
    y = softmax(x)

    print(f"softmax(x): {y}")
    print(f"sum(softmax(x))): {np.sum(y)}")


if __name__ == "__main__":
    main()
