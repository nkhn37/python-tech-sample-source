"""scikit-learn
主成分分析による次元削減

[説明ページ]
https://tech.nkhn37.net/scikit-learn-pca/#i-3
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

    # ===== 主成分分析の実行(1次元)
    pca = PCA(n_components=1)
    pca.fit(data)

    # 結果の表示
    print(f"主成分: \n{pca.components_}")
    print(f"分散: \n{pca.explained_variance_}")
    print(f"寄与率: \n{pca.explained_variance_ratio_}")

    # ===== 一次元へ変換
    data_pca = pca.transform(data)
    # 2次元空間へ戻してみて確認してみる
    data_new = pca.inverse_transform(data_pca)
    plt.scatter(data_new[:, 0], data_new[:, 1])

    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    main()
