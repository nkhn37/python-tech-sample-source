"""自己符号化器(AutoEncoder)の実装

[説明ページ]
https://tech.nkhn37.net/tensorflow-keras-autoencoder/#TensorFlowKerasAutoEncoder
"""
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist


def main():
    """メイン関数"""
    # ===== MNIST(エムニスト)データの読込
    (train_imgs, _), (test_imgs, _) = mnist.load_data()
    train_imgs = train_imgs.astype("float32") / 255
    test_imgs = test_imgs.astype("float32") / 255
    train_imgs = train_imgs.reshape((60000, 784))
    test_imgs = test_imgs.reshape((10000, 784))
    # 訓練データの一部(20%)を評価データとして使う
    idx = int(train_imgs.shape[0] * 0.2)
    train_imgs, val_imgs = train_imgs[idx:], train_imgs[:idx]

    # ===== AutoEncoderの構築
    # 隠れ層の次元
    encoding_dim = 32
    # 入力データ
    inputs = keras.Input(shape=(784,))
    # エンコード部
    encoded = layers.Dense(encoding_dim, activation="relu")(inputs)
    # デコード部
    decoded = layers.Dense(784, activation="sigmoid")(encoded)

    # ===== モデルの構築
    # AutoEncoderモデルの作成
    autoencoder = keras.Model(inputs=inputs, outputs=decoded, name="AutoEncoder")
    print(autoencoder.summary())
    keras.utils.plot_model(autoencoder, "autoencoder.png", show_shapes=True)

    # Encoderモデル
    encoder = keras.Model(inputs=inputs, outputs=encoded, name="Encoder")
    # print(encoder.summary())
    # keras.utils.plot_model(encoder, "encoder.png", show_shapes=True)

    # Decoderモデル
    encoded_input = keras.Input(shape=(encoding_dim,))
    decoder_layer = autoencoder.layers[-1](encoded_input)
    decoder = keras.Model(inputs=encoded_input, outputs=decoder_layer, name="Decoder")
    # print(decoder.summary())
    # keras.utils.plot_model(decoder, "decoder.png", show_shapes=True)

    # ===== オプティマイザ、損失関数、指標を設定してコンパイル
    autoencoder.compile(optimizer="adam", loss="binary_crossentropy")

    # ===== fitを使ったモデルの訓練
    num_epochs = 20
    history = autoencoder.fit(
        train_imgs,
        train_imgs,
        epochs=num_epochs,
        batch_size=128,
        validation_data=(val_imgs, val_imgs),
    )

    # ===== history情報の可視化
    # 損失関数(loss)の履歴
    loss = history.history["loss"]
    val_loss = history.history["val_loss"]
    # 損失関数の履歴描画
    x_epoch = range(1, num_epochs + 1)
    plt.plot(x_epoch, loss, "r", label="training loss")
    plt.plot(x_epoch, val_loss, "b", label="validation loss")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.legend()
    plt.show()

    # ====== テスト画像を使ってエンコード／デコードの実行
    # エンコード
    encoded_imgs = encoder.predict(test_imgs)
    # デコード
    decoded_imgs = decoder.predict(encoded_imgs)

    # ===== テスト画像のエンコード、デコード結果を表示
    disp_n = 5
    plt.figure(figsize=(10, 5))
    for i in range(disp_n):
        # 元画像の表示
        ax = plt.subplot(3, disp_n, i + 1)
        plt.imshow(test_imgs[i].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # エンコード値の表示
        ax = plt.subplot(3, disp_n, i + 1 + disp_n)
        plt.imshow(encoded_imgs[i].reshape(1, encoding_dim))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # 復元画像の表示
        ax = plt.subplot(3, disp_n, i + 1 + 2 * disp_n)
        plt.imshow(decoded_imgs[i].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

    plt.show()


if __name__ == "__main__":
    main()
