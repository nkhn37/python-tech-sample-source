"""k近傍法(k-NN)を用いたデータ分類方法

[説明ページ]
https://tech.nkhn37.net/scikit-learnk-kneighborsclassifier/#i
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def main():
    """メイン関数"""
    np.random.seed(1)

    # ===== データの用意
    data, label = make_classification(
        n_samples=1000,
        n_classes=2,
        n_features=4,
        n_informative=4,
        n_redundant=0,
    )
    # データセットを訓練用、テスト用に分割する
    train_data, test_data, train_label, test_label = train_test_split(data, label)

    # ===== 複数のkで性能が分類性能がどのように変わるか確認
    k_list = [k for k in range(1, 11)]
    acc_list = []

    # ===== kを変えながらモデルを順番に学習
    for k in k_list:
        # モデルの構築
        model = KNeighborsClassifier(n_neighbors=k)
        # モデルの学習
        model.fit(train_data, train_label)
        # 正解率の評価
        acc_list.append(model.score(test_data, test_label))

    # ===== 正解率をプロットする
    plt.plot(k_list, acc_list)
    plt.title("accuracy list")
    plt.xlabel("n_neighbors")
    plt.ylabel("accuracy")
    plt.show()


if __name__ == "__main__":
    main()
