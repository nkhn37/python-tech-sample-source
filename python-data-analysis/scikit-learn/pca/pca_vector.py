"""scikit-learn
主成分分析後に主成分ベクトルを表示してみる

[説明ページ]
https://tech.nkhn37.net/scikit-learn-pca/#i-2
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA


def draw_vector(pt_from, pt_to, ax=None):
    """ベクトル描画関数

    Args:
        pt_from: 矢印の始点座標
        pt_to: 矢印の終点座標
        ax: 描画対象axis (デフォルト:None)
    """

    if ax is None:
        ax = plt.gca()
    arrowprops = dict(arrowstyle="->", linewidth=2, shrinkA=0, shrinkB=0)
    ax.annotate("", pt_to, pt_from, arrowprops=arrowprops)


def main():
    """メイン関数"""

    np.random.seed(123)

    # ===== データの作成と描画
    n_point = 200
    data = np.dot(np.random.rand(2, 2), np.random.randn(2, n_point)).T
    plt.scatter(data[:, 0], data[:, 1])
    plt.axis("equal")

    # ===== 主成分分析の実行
    pca = PCA(n_components=2)
    pca.fit(data)

    # 結果の表示
    print(f"主成分: \n{pca.components_}")
    print(f"分散: \n{pca.explained_variance_}")
    print(f"寄与率: \n{pca.explained_variance_ratio_}")

    # ===== 主成分ベクトルを表示してみる
    for var, vector in zip(pca.explained_variance_, pca.components_):
        # 標準偏差分の長さのベクトルを作成
        vec = vector * np.sqrt(var)
        draw_vector(pca.mean_, pca.mean_ + vec)
    plt.show()

    # =====
    data_pca = pca.transform(data)
    plt.scatter(data_pca[:, 0], data_pca[:, 1])
    plt.axis("equal")
    plt.xlabel("component1")
    plt.ylabel("component2")
    plt.show()


if __name__ == "__main__":
    main()
