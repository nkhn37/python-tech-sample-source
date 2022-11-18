"""scikit-learn
サポートベクターマシンを使用した分類 sklearn.svm.SVC
非線形分類をする場合

[説明ページ]
https://tech.nkhn37.net/scikit-learn-svm/#i-2
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_gaussian_quantiles
from sklearn.svm import SVC


def show_svm_result(svm_model, ax=None):
    """SVMの結果を表示する

    Args:
        svm_model: SVM学習結果モデル
        ax: axisの指定 (デフォルト: None)
    """
    if ax is None:
        ax = plt.gca()
    n_grid = 50

    xlim, ylim = ax.get_xlim(), ax.get_ylim()
    x = np.linspace(xlim[0], xlim[1], n_grid)
    y = np.linspace(ylim[0], ylim[1], n_grid)
    ygrid, xgrid = np.meshgrid(y, x)
    xygrid = np.vstack([xgrid.ravel(), ygrid.ravel()]).T
    decision = svm_model.decision_function(xygrid).reshape(xgrid.shape)

    # 境界線、マージンを表示
    ax.contour(
        xgrid,
        ygrid,
        decision,
        colors="k",
        levels=[-1, 0, 1],
        linestyles=["--", "-", "--"],
        alpha=0.5,
    )
    # サポートベクターを表示
    ax.scatter(
        svm_model.support_vectors_[:, 0],
        svm_model.support_vectors_[:, 1],
        s=100,
        linewidth=1,
        facecolor="none",
        edgecolor="r",
        label="Support Vector",
    )
    ax.legend()
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)


def main():
    """メイン関数"""
    np.random.seed(0)

    # ===== データの生成
    data, label = make_gaussian_quantiles(n_samples=100, n_classes=2, n_features=2)

    plt.scatter(data[label == 0, 0], data[label == 0, 1], marker="o")
    plt.scatter(data[label == 1, 0], data[label == 1, 1], marker="^")

    # ===== サポートベクターマシンを用いた学習
    model = SVC(C=1.0e10)
    model.fit(data, label)
    print(model)
    print(model.support_vectors_)

    # ===== svmの結果表示
    show_svm_result(model)

    # 描画
    plt.show()


if __name__ == "__main__":
    main()
