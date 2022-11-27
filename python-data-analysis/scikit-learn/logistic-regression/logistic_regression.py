"""LogisticRegressionでロジスティック回帰をする方法

[説明ページ]
https://tech.nkhn37.net/scikit-learn-logisticregression/#i-2
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression


def main():
    """メイン関数"""
    np.random.seed(0)

    # ===== データの生成
    data, label = make_blobs(n_samples=1000, centers=2, cluster_std=0.5)
    plt.scatter(data[label == 0, 0], data[label == 0, 1], marker="o")
    plt.scatter(data[label == 1, 0], data[label == 1, 1], marker="^")

    # ===== ロジスティック回帰を用いた学習
    model = LogisticRegression()
    model.fit(data, label)

    # ===== 分類結果の可視化
    xmin, xmax = data[:, 0].min() - 1, data[:, 0].max() + 1
    ymin, ymax = data[:, 1].min() - 1, data[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(xmin, xmax, 0.01), np.arange(ymin, ymax, 0.01))
    zz = model.predict(np.array([xx.ravel(), yy.ravel()]).T).reshape(xx.shape)
    plt.contourf(xx, yy, zz, alpha=0.5)
    plt.title("Logistic Regression")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
