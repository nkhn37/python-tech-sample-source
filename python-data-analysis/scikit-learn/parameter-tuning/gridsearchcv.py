"""グリッドサーチでパラメータチューニング

[説明ページ]
https://tech.nkhn37.net/scikit-learn-gridsearchcv-randomizedsearchcv/#GridSearchCV
"""
import numpy as np
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split


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

    # ===== モデルのハイパーパラメータ候補値を設定する
    model_param_set = {
        SVC(): {
            "kernel": ["linear", "poly", "rbf", "sigmoid"],
            "C": [10**i for i in range(-5, 5)],
            "decision_function_shape": ["ovo", "ovr"],
            "random_state": [seed],
        }
    }

    # ===== グリッドサーチ
    max_score = 0
    best_param = None

    for model, param in model_param_set.items():
        # グリッドサーチを生成
        clf = GridSearchCV(model, param)
        # 訓練の実行
        clf.fit(train_data, train_label)
        # データの予測と正解率の計算
        pred = clf.predict(test_data)
        score = accuracy_score(test_label, pred)
        # 最高スコアの更新
        if max_score < score:
            max_score = score
            best_param = clf.best_params_

        # # パラメータの組み合わせを確認
        # print(clf.cv_results_["params"])

    print(f"ハイパーパラメータ: {best_param}")
    print(f"最高スコア: {max_score}")


if __name__ == "__main__":
    main()
