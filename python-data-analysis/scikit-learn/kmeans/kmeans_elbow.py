"""KMeansでエルボー法によるクラスタ数の決定

[説明ページ]
https://tech.nkhn37.net/scikit-learn-kmeans/#i-3
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

    # ===== エルボー法
    sse = []
    for k in range(1, 11):
        km = KMeans(n_clusters=k)
        km.fit(data)
        sse.append(km.inertia_)

    # ===== SSE値をプロットする
    plt.plot(range(1, 11), sse, "o-")
    plt.title("elbow method")
    plt.xlabel("number of clusters")
    plt.ylabel("sse")
    plt.show()


if __name__ == "__main__":
    main()
