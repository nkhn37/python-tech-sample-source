"""scikit-learn
主成分分析の基本的な使い方 sklearn.decomposition.PCA

[説明ページ]
https://tech.nkhn37.net/scikit-learn-pca/#sklearndecompositionPCA
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA


def main():
    """メイン関数"""

    np.random.seed(123)

    # ===== データの作成と描画
    n_point = 200
    data = np.dot(np.random.rand(2, 2), np.random.randn(2, n_point)).T
    plt.scatter(data[:, 0], data[:, 1])
    plt.axis("equal")
    plt.show()

    # ===== 主成分分析の実行
    pca = PCA(n_components=2)
    pca.fit(data)

    # 結果の表示
    print(f"主成分: \n{pca.components_}")
    print(f"分散: \n{pca.explained_variance_}")
    print(f"寄与率: \n{pca.explained_variance_ratio_}")


if __name__ == "__main__":
    main()
