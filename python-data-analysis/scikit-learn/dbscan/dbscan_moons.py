"""DBSCANによるクラスタリング

[説明ページ]
https://tech.nkhn37.net/scikit-learn-dbscan/#DBSCANsklearnclusterDBSCAN
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons


def main():
    """メイン関数"""
    np.random.seed(1)

    # ===== データの生成
    data, label = make_moons(n_samples=500, noise=0.05)

    # ===== DBSCANでのクラスタリング
    dbscan = DBSCAN(eps=0.2, min_samples=5)
    pred = dbscan.fit_predict(data)
    n_c = set(pred)

    # ===== クラスタリング結果を描画する
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    # 元データを表示する
    ax[0].scatter(data[:, 0], data[:, 1])
    ax[0].set_title("original data")
    # クラスタリング結果を表示する
    for i in n_c:
        ax[1].scatter(data[pred == i, 0], data[pred == i, 1])
    ax[1].set_title("DBSCAN clustering")
    plt.show()


if __name__ == "__main__":
    main()
