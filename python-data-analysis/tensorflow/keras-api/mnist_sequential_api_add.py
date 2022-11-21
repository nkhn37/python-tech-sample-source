"""Keras API
Sequential APIでのMNIST手書き文字分類 実装例
(addで層を追加していく場合)

[説明ページ]
https://tech.nkhn37.net/tensorflow-keras-sequential-functional-subclassing-api/#i-3
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
    # addで層を追加する場合
    model = keras.Sequential()
    model.add(keras.Input(shape=(28 * 28,)))
    model.add(layers.Dense(256, activation="relu"))
    model.add(layers.Dense(256, activation="relu"))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(10, activation="softmax"))

    # ===== optimizer、損失関数、指標を指定してコンパイル
    model.compile(
        optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
    )
    print(model.summary())

    # ===== fitを使ったモデルの訓練
    history = model.fit(
        train_imgs, train_labels, epochs=5, validation_data=(val_imgs, val_labels)
    )

    # ===== evaluateを使ったテストデータでの評価
    result = model.evaluate(test_imgs, test_labels)
    print(result)

    # ===== predictを使って予測結果を表示
    preds = model.predict(test_imgs)
    print(f"予測: {np.argmax(preds[0])}, 正解: {test_labels[0]}")


if __name__ == "__main__":
    main()
