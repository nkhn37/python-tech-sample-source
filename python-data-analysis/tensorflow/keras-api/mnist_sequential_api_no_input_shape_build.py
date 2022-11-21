"""Keras API
Sequential APIでのMNIST手書き文字分類 実装例
モデルの重みが計算されるのはbuild()が呼び出されたタイミング

[説明ページ]
https://tech.nkhn37.net/tensorflow-keras-sequential-functional-subclassing-api/#build
"""
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist


def main():
    """メイン関数"""

    # ===== MNISTデータを読み込み＆正規化
    (train_imgs, train_labels), (test_imgs, test_labels) = mnist.load_data()
    train_imgs = train_imgs.reshape((60000, 28 * 28)).astype("float32") / 255
    test_imgs = test_imgs.reshape((10000, 28 * 28)).astype("float32") / 255
    # 訓練データの一部(20%)を評価データとして使う
    idx = int(train_imgs.shape[0] * 0.2)
    train_imgs, val_imgs = train_imgs[idx:], train_imgs[:idx]
    train_labels, val_labels = train_labels[idx:], train_labels[:idx]

    # ===== モデルを構築する（Sequential APIを使用）
    # Inputの形状を指定しない
    model = keras.Sequential(
        [
            layers.Dense(256, activation="relu"),
            layers.Dense(256, activation="relu"),
            layers.Dropout(0.5),
            layers.Dense(10, activation="softmax"),
        ]
    )

    # ===== buildを呼び出すと重みが作成される。
    model.build(input_shape=(None, 28 * 28))
    print(model.weights)


if __name__ == "__main__":
    main()
