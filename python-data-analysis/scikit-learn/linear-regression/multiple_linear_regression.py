"""scikit-learn
線形重回帰分析の実装方法

[説明ページ]
https://tech.nkhn37.net/scikit-learn-linearregression-basic/#i-5
"""
import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def main():
    rs = np.random.RandomState(123)

    # ===== 線形重回帰を行うためのデータを生成する
    bias = 5.0
    x, y, coef = make_regression(
        n_samples=10000,
        n_features=10,
        n_informative=3,
        n_targets=1,
        coef=True,
        bias=bias,
        noise=5.0,
        random_state=rs,
    )
    np.set_printoptions(precision=3, suppress=True)
    print(f"true coef: {coef}")
    print(f"true bias: {bias:.3f}")

    # 学習用データとテスト用データを分割する
    train_x, test_x, train_y, test_y = train_test_split(x, y, random_state=rs)

    # ===== 線形重回帰モデルを生成する
    model = LinearRegression(fit_intercept=True)

    # ===== モデルを学習する
    model.fit(train_x, train_y)

    # パラメータを表示する
    print(f"coef: {model.coef_}")
    print(f"bias: {model.intercept_:.3f}")
    print(f"R2: {model.score(test_x, test_y):.3f}")


if __name__ == "__main__":
    main()
