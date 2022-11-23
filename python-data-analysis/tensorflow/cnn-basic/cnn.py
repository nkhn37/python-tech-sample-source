"""CNN(畳み込みニューラルネットワーク)による画像分類
実装例

[CNN概要説明]
https://tech.nkhn37.net/tensorflow-keras-cnn-basic-mnist/#CNN-2

[実装例の説明]
https://tech.nkhn37.net/tensorflow-keras-cnn-basic-mnist/#i-4
"""
import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist


def main():
    """メイン関数"""

    # ===== MNIST(エムニスト)データの読込
    (train_imgs, train_labels), (test_imgs, test_labels) = mnist.load_data()
    train_imgs = train_imgs.reshape((60000, 28, 28, 1))
    test_imgs = test_imgs.reshape((10000, 28, 28, 1))
    # 訓練データの一部(20%)を評価データとして使う
    idx = int(train_imgs.shape[0] * 0.2)
    train_imgs, val_imgs = train_imgs[idx:], train_imgs[:idx]
    train_labels, val_labels = train_labels[idx:], train_labels[:idx]

    # ===== CNNモデルの構築
    # MNIST画像は28×28でチャンネルは1
    inputs = keras.Input(shape=(28, 28, 1))
    # 前処理0~1へ正規化
    x = layers.Rescaling(1.0 / 255)(inputs)
    # 畳み込み層とプーリング層の定義
    x = layers.Conv2D(32, kernel_size=3, activation="relu")(x)
    x = layers.MaxPooling2D(pool_size=2)(x)
    x = layers.Conv2D(64, kernel_size=3, activation="relu")(x)
    x = layers.MaxPooling2D(pool_size=2)(x)
    x = layers.Conv2D(128, kernel_size=3, activation="relu")(x)
    x = layers.MaxPooling2D(pool_size=2)(x)
    # 平坦化する
    x = layers.Flatten()(x)
    # ドロップアウトを設定
    x = layers.Dropout(0.5)(x)
    # 分類のために10のノードに接続
    outputs = layers.Dense(10, activation="softmax")(x)

    # モデルの作成
    model = keras.Model(inputs=inputs, outputs=outputs)
    # モデル構成の表示&画像保存
    print(model.summary())
    keras.utils.plot_model(model, "mnist_cnn_classifier.png", show_shapes=True)

    # ===== オプティマイザ、損失関数、指標を設定してコンパイル
    model.compile(
        optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
    )

    # ===== fitを使ったモデルの訓練
    num_epochs = 5
    history = model.fit(
        train_imgs,
        train_labels,
        epochs=num_epochs,
        batch_size=32,
        validation_data=(val_imgs, val_labels),
    )

    # ===== history情報の可視化
    # 損失関数(loss)の履歴
    loss = history.history["loss"]
    val_loss = history.history["val_loss"]
    # 正解率(accuracy)の履歴
    acc = history.history["accuracy"]
    val_acc = history.history["val_accuracy"]

    # 損失関数の履歴描画
    x_epoch = range(1, num_epochs + 1)
    plt.plot(x_epoch, loss, "r", label="training loss")
    plt.plot(x_epoch, val_loss, "b", label="validation loss")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.legend()
    # 正解率の履歴描画
    plt.figure()
    plt.plot(x_epoch, acc, "r", label="training acc")
    plt.plot(x_epoch, val_acc, "b", label="validation acc")
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")
    plt.legend()

    plt.show()

    # ===== evaluateを使ったテストデータでの評価
    result = model.evaluate(test_imgs, test_labels)
    print(result)

    # ===== predictを使って予測結果を表示
    preds = model.predict(test_imgs)
    print(f"予測: {np.argmax(preds[0])}, 正解: {test_labels[0]}")


if __name__ == "__main__":
    main()
