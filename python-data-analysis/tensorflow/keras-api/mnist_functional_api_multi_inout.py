"""Keras API
Functional APIでのMNIST手書き文字分類 実装例
(複数の入出力を持つようなモデルの設計)

[説明ページ]
https://tech.nkhn37.net/tensorflow-keras-sequential-functional-subclassing-api/#i-6
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
    # 複数の入出力を持つようなモデルの設計
    inputs1 = keras.Input(shape=(28 * 28,))
    inputs2 = keras.Input(shape=(10,))
    inputs = layers.Concatenate()([inputs1, inputs2])
    x = layers.Dense(256, activation="relu")(inputs)
    x = layers.Dense(256, activation="relu")(x)
    x = layers.Dropout(0.5)(x)
    outputs1 = layers.Dense(10, activation="softmax")(x)
    outputs2 = layers.Dense(1, activation="sigmoid")(x)
    model = keras.Model(inputs=[inputs1, inputs2], outputs=[outputs1, outputs2])
    print(model.summary())

    # モデルを画像で可視化する
    keras.utils.plot_model(model, "mnist_classifier_multi.png", show_shapes=True)


if __name__ == "__main__":
    main()
