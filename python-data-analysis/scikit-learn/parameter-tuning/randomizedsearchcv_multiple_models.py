"""パラメータチューニング
複数モデルを比較する方法（ランダムサーチを使用）

[説明ページ]
https://tech.nkhn37.net/scikit-learn-gridsearchcv-randomizedsearchcv/#i-9
"""
import numpy as np
import scipy.stats
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


def main():
    """メイン関数"""
    seed = 0
    np.random.seed(seed)

    # ===== データの生成
    data = load_digits()
    # 学習データとテストデータに分割
    train_data, test_data, train_label, test_label = train_test_split(
        data.data, data.target, random_state=seed
    )

    # ===== モデルのハイパーパラメータ候補情報
    model_param_set = {
        # 非線形SVM
        SVC(): {
            "C": scipy.stats.uniform(0, 100000),
            "kernel": ["rbf", "poly"],
            "decision_function_shape": ["ovo", "ovr"],
            "random_state": [seed],
        },
        # 決定木
        DecisionTreeClassifier(): {
            "max_depth": [i for i in range(1, 21)],
            "random_state": [seed],
        },
        # ランダムフォレスト
        RandomForestClassifier(): {
            "n_estimators": [i for i in range(1, 51)],
            "max_depth": [i for i in range(1, 21)],
            "random_state": [seed],
        },
    }

    # ===== ランダムサーチで最適モデルを調べる
    max_score = 0
    best_method = None
    best_param = None

    for model, param in model_param_set.items():
        # print(model, param)
        method = model.__class__.__name__
        # ランダムサーチを生成
        clf = RandomizedSearchCV(model, param)
        # 訓練の実行
        clf.fit(train_data, train_label)
        # データの予測と正解率の計算
        pred = clf.predict(test_data)
        score = accuracy_score(test_label, pred)
        # 最高スコアの更新
        if max_score < score:
            max_score = score
            best_method = method
            best_param = clf.best_params_

        # # パラメータの組み合わせを確認
        # print(clf.cv_results_["params"])

    print("==========")
    print(f"学習モデル: {best_method}")
    print(f"パラメーター: {best_param}")
    print(f"最高スコア: {max_score}")
    print("==========")


if __name__ == "__main__":
    main()
