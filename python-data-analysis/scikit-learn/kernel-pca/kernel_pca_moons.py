"""Kernel PCAでカーネル主成分分析
moonsデータでの実装例

[説明ページ]
https://tech.nkhn37.net/scikit-learn-kernelpca/#moons
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_moons
from sklearn.decomposition import KernelPCA


def main():
    """メイン関数"""
    np.random.seed(0)

    # ===== データの用意・表示
    data, label = make_moons(n_samples=100, noise=0.01)
    plt.scatter(data[label == 0, 0], data[label == 0, 1], marker="x")
    plt.scatter(data[label == 1, 0], data[label == 1, 1], marker="^")
    plt.title("moon data")

    # ===== カーネルPCAのモデル生成・学習
    k_pca = KernelPCA(n_components=2, kernel="rbf", gamma=15)
    k_pca.fit(data, label)

    # ===== 主成分軸への変換
    trans_data = k_pca.transform(data)

    # ===== 変換結果を表示
    plt.figure()
    plt.scatter(trans_data[label == 0, 0], trans_data[label == 0, 1], marker="x")
    plt.scatter(trans_data[label == 1, 0], trans_data[label == 1, 1], marker="^")
    plt.title("kernel pca")

    plt.show()


if __name__ == "__main__":
    main()
