"""線形回帰の正則化手法: リッジ(Ridge)回帰

[説明ページ]
https://tech.nkhn37.net/scikit-learn-lasso-ridge-elasticnet/#Ridge
"""
import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split


def main():
    """メイン関数"""
    np.random.seed(123)
    np.set_printoptions(precision=3, suppress=True)

    # ===== 線形回帰を行うためのデータを生成する
    bias = 5.0
    noise = 50.0
    x, y, coef = make_regression(
        n_samples=100,
        n_features=10,
        n_informative=5,
        n_targets=1,
        coef=True,
        bias=bias,
        noise=noise,
    )
    print(f"true coef: {coef}")
    print(f"true bias: {bias:.3f}")

    # 学習用データとテスト用データを分割する
    train_x, test_x, train_y, test_y = train_test_split(x, y)

    # ===== Ridge回帰モデルを生成する
    model = Ridge(alpha=1.0)

    # ===== モデルを学習する
    model.fit(train_x, train_y)

    # 推定結果の表示
    print(f"coef: {model.coef_}")
    print(f"bias: {model.intercept_:.3f}")
    print(f"R2: {model.score(test_x, test_y):.3f}")


if __name__ == "__main__":
    main()
