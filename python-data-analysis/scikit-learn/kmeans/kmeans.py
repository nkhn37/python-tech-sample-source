"""KMeansでk-means法によるクラスタリングをする方法

[説明ページ]
https://tech.nkhn37.net/scikit-learn-kmeans/#k-menassklearnclusterKMeans
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans


def main():
    """メイン関数"""
    np.random.seed(1)

    # ===== データの生成
    k = 5
    data, label = make_blobs(n_samples=500, n_features=2, centers=k, cluster_std=1.0)

    # ===== k-meansクラスタリング
    km = KMeans(n_clusters=k)
    pred = km.fit_predict(data)

    # ===== SSE値を出力
    print(f"SSE: {km.inertia_:.2f}")

    # ===== クラスタリング結果を描画する
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    # 元データを表示する
    ax[0].scatter(data[:, 0], data[:, 1])
    ax[0].set_title("original data")
    # クラスタリング結果を表示する
    for i in range(k):
        ax[1].scatter(data[pred == i, 0], data[pred == i, 1])
    ax[1].set_title("k-means clustering")
    plt.show()


if __name__ == "__main__":
    main()
