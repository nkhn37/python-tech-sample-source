"""訓練済みモデルVGG16での転移学習

[説明ページ]
https://tech.nkhn37.net/tensorflow-keras-transfer-learning-vgg16/#i-2
"""
import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.optimizers import SGD


def main():
    """メイン関数"""

    (train_imgs, train_labels), (test_imgs, test_labels) = cifar10.load_data()
    # 訓練データの一部(20%)を評価データとして使う
    idx = int(train_imgs.shape[0] * 0.2)
    train_imgs, val_imgs = train_imgs[idx:], train_imgs[:idx]
    train_labels, val_labels = train_labels[idx:], train_labels[:idx]

    # ===== VGG16で事前に学習されたモデルを読み込む
    vgg16 = VGG16(include_top=False, weights="imagenet", input_shape=(32, 32, 3))

    # ===== 新しい出力用分類モデルを作成する
    # VGG16の出力を平坦化して全結合層へ接続
    x = layers.Flatten()(vgg16.output)
    x = layers.Dense(256, activation="relu")(x)
    x = layers.Dropout(0.5)(x)
    # 分類のために10ノードに接続
    outputs = layers.Dense(10, activation="softmax")(x)

    # モデルの作成
    model = keras.Model(inputs=vgg16.input, outputs=outputs)

    # 0~18までのlayerがVGG16に関連するので重みを固定する
    for layer in model.layers[:19]:
        layer.trainable = False

    # モデル構成の表示&画像保存
    print(model.summary())
    keras.utils.plot_model(
        model, "transfer_learning_vgg16_cifar10.png", show_shapes=True
    )

    # ===== オプティマイザ、損失関数、指標を設定してコンパイル
    # 転移学習の場合、最適化関数はSGDの選択がよいとされている
    model.compile(
        optimizer=SGD(learning_rate=1e-4, momentum=0.9),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )

    # ===== fitを使ったモデルの訓練
    # 設定
    num_epochs = 10
    callbacks = [
        keras.callbacks.ModelCheckpoint("vgg16_cifar10.keras", save_best_only=True)
    ]
    # 訓練の実行
    history = model.fit(
        train_imgs,
        train_labels,
        epochs=num_epochs,
        batch_size=32,
        validation_data=(val_imgs, val_labels),
        callbacks=callbacks,
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
