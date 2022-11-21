"""Keras API
Functional APIでのMNIST手書き文字分類 実装例
(plot_modelでモデル形状を画像化する)

[説明ページ]
https://tech.nkhn37.net/tensorflow-keras-sequential-functional-subclassing-api/#i-5
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

    # ===== モデルを構築する（Functional APIを使用）
    inputs = keras.Input(shape=(28 * 28,))
    x = layers.Dense(256, activation="relu")(inputs)
    x = layers.Dense(256, activation="relu")(x)
    x = layers.Dropout(0.5)(x)
    outputs = layers.Dense(10, activation="softmax")(x)
    model = keras.Model(inputs=inputs, outputs=outputs)
    print(model.summary())

    # モデルを画像で可視化する
    keras.utils.plot_model(model, "mnist_classifier.png", show_shapes=True)


if __name__ == "__main__":
    main()
