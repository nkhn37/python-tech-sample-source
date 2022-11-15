"""sckit-learn
線形単回帰分析の実装方法

[説明ページ]
https://tech.nkhn37.net/scikit-learn-linearregression-basic/#i-2
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def main():
    rs = np.random.RandomState(123)

    # ===== 線形回帰を行うためのデータを生成する
    bias = 5.0
    x, y, coef = make_regression(
        n_samples=100,
        n_features=1,
        n_targets=1,
        coef=True,
        bias=bias,
        noise=5.0,
        random_state=rs,
    )
    np.set_printoptions(precision=3, suppress=True)
    print(f"true coef: {coef:.3f}")
    print(f"true bias: {bias:.3f}")
    plt.plot(x, y, ".")

    # 訓練用データとテスト用データを分割する
    train_x, test_x, train_y, test_y = train_test_split(x, y, random_state=rs)

    # ===== 線形単回帰モデルを生成する
    model = LinearRegression(fit_intercept=True)

    # ===== モデルを学習する
    model.fit(train_x, train_y)

    # 推定結果の表示
    print(f"coef: {model.coef_}")
    print(f"bias: {model.intercept_:.3f}")
    print(f"R2: {model.score(test_x, test_y):.3f}")

    # ===== 線形回帰結果の線を引く
    xfit = np.linspace(np.min(x), np.max(x), 1000)
    # Y軸はpredictを実行して計算
    yfit = model.predict(xfit[:, np.newaxis])
    plt.plot(xfit, yfit)
    plt.show()


if __name__ == "__main__":
    main()
