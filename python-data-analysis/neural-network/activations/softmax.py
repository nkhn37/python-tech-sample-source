"""ニューラルネットワークの活性化関数
softmax関数

[説明ページ]
https://tech.nkhn37.net/neural-network-activations/#softmax
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
    
    x = np.array([0.5, 2.8, 5.0, 1.0, 3.0])
    y = softmax(x)

    print(f"softmax(x): {y}")
    print(f"sum(softmax(x))): {np.sum(y)}")


if __name__ == "__main__":
    main()
