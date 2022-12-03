"""変分自己符号化器(VAE: Variational AutoEncoder)の実装

[説明ページ]
https://tech.nkhn37.net/tensorflow-keras-vae/#TensorFlowKerasVAEVariationalAutoEncoder
"""
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist


class VAE(keras.Model):
    """VAE (Variational Auto Encoder)モデル"""

    def __init__(self, encoder, decoder, **kwargs):
        super(VAE, self).__init__(**kwargs)
        self.encoder = encoder
        self.decoder = decoder
        self.sampler = Sampler()
        # 損失関数トレース用
        self.total_loss_tracker = keras.metrics.Mean(name="total_loss")
        self.reconstruction_loss_tracker = keras.metrics.Mean(
            name="reconstruction_loss"
        )
        self.kl_loss_tracker = keras.metrics.Mean(name="kl_loss")

    @property
    def metrics(self):
        return [
            self.total_loss_tracker,
            self.reconstruction_loss_tracker,
            self.kl_loss_tracker,
        ]

    def train_step(self, data):
        """訓練ステップ
        :param data: 入力データ
        :return: 損失値
        """
        with tf.GradientTape() as tape:
            z_mean, z_log_var = self.encoder(data)
            z = self.sampler(z_mean, z_log_var)
            reconstructed_data = self.decoder(z)

            # 誤差の計算
            reconstruction_loss = tf.reduce_mean(
                tf.reduce_sum(
                    keras.losses.binary_crossentropy(data, reconstructed_data),
                    axis=(1, 2),
                )
            )
            # KLダイバージェンス
            kl_loss = 0.5 * (-z_log_var + tf.exp(z_log_var) + tf.square(z_mean) - 1)

            # 総誤差
            total_loss = reconstruction_loss + kl_loss

        # 勾配計算
        grads = tape.gradient(total_loss, self.trainable_weights)
        self.optimizer.apply_gradients(zip(grads, self.trainable_weights))
        # 誤差の設定
        self.total_loss_tracker.update_state(total_loss)
        self.reconstruction_loss_tracker.update_state(reconstruction_loss)
        self.kl_loss_tracker.update_state(kl_loss)

        ret = {
            "total_loss": self.total_loss_tracker.result(),
            "reconstruction_loss": self.reconstruction_loss_tracker.result(),
            "kl_loss": self.kl_loss_tracker.result(),
        }
        return ret


class Sampler(layers.Layer):
    """潜在変数zのサンプル実行クラス"""

    def call(self, z_mean, z_log_var):
        batch_size = tf.shape(z_mean)[0]
        z_size = tf.shape(z_mean)[1]

        # 正規ガウス分布からランダムな値(epsilon)を抽出
        epsilon = tf.random.normal(shape=(batch_size, z_size))
        # サンプリング値を使用してzを計算して返却
        return z_mean + tf.exp(0.5 * z_log_var) * epsilon


def main():
    """メイン関数"""
    # ===== MNIST(エムニスト)データの読込
    (train_imgs, _), (test_imgs, _) = mnist.load_data()
    # 全ての画像を使って生成モデルを訓練するため訓練データとテストデータを結合
    train_imgs = np.concatenate([train_imgs, test_imgs], axis=0)
    # reshapeと正規化(0~1)
    train_imgs = train_imgs.reshape((70000, 28, 28, 1)).astype("float32") / 255

    # ===== Encoder(エンコーダ)ネットワークの構築
    # 2次元の潜在空間
    latent_dim = 2
    # ネットワークの構築
    encoder_inputs = keras.Input(shape=(28, 28, 1))
    x = layers.Conv2D(32, 3, activation="relu", strides=2, padding="same")(
        encoder_inputs
    )
    x = layers.Conv2D(64, 3, activation="relu", strides=2, padding="same")(x)
    x = layers.Flatten()(x)
    x = layers.Dense(16, activation="relu")(x)
    # 平均と分散
    z_mean = layers.Dense(latent_dim, name="z_mean")(x)
    z_log_var = layers.Dense(latent_dim, name="z_log_var")(x)
    # Encoderモデルの構築
    encoder = keras.Model(
        inputs=encoder_inputs, outputs=[z_mean, z_log_var], name="encoder"
    )
    print(encoder.summary())
    keras.utils.plot_model(encoder, "encoder.png", show_shapes=True)

    # ===== Decoder(デコーダ)ネットワークの構築
    latent_inputs = keras.Input(shape=(latent_dim,))
    # ネットワークの構築
    # Encoderと逆の手順で画像に戻していく
    x = layers.Dense(7 * 7 * 64, activation="relu")(latent_inputs)
    x = layers.Reshape((7, 7, 64))(x)
    x = layers.Conv2DTranspose(64, 3, activation="relu", strides=2, padding="same")(x)
    x = layers.Conv2DTranspose(32, 3, activation="relu", strides=2, padding="same")(x)
    # 最終的には元画像と同じ(28, 28, 1)の形状にする
    decoder_outputs = layers.Conv2D(1, 3, activation="sigmoid", padding="same")(x)
    # Decoderモデルの構築
    decoder = keras.Model(inputs=latent_inputs, outputs=decoder_outputs, name="decoder")
    print(decoder.summary())
    keras.utils.plot_model(decoder, "decoder.png", show_shapes=True)

    # ===== VAEモデルの生成
    vae = VAE(encoder, decoder)

    # ===== モデルのコンパイル
    vae.compile(optimizer="adam", run_eagerly=True)

    # ===== モデルの学習
    n_epochs = 30
    history = vae.fit(train_imgs, epochs=n_epochs, batch_size=128)

    # ===== 潜在空間のサンプルから画像を生成する
    n_imgs = 30
    img_size = 28
    figure_data = np.zeros((img_size * n_imgs, img_size * n_imgs))

    # 潜在変数zのグリッド
    z_grid_1 = np.linspace(-1, 1, n_imgs)
    z_grid_2 = np.linspace(-1, 1, n_imgs)

    # 各z点における画像を生成モデルから作成
    for i, z_1 in enumerate(z_grid_1):
        for j, z_2 in enumerate(z_grid_2):
            z = np.array([[z_1, z_2]])
            decoded_img = vae.decoder.predict(z)
            img = decoded_img[0].reshape(img_size, img_size)

            # figure_dataの該当位置に埋め込み
            figure_data[
                i * img_size : (i + 1) * img_size, j * img_size : (j + 1) * img_size
            ] = img

    # 軸の値を生成
    start_range = img_size // 2
    end_range = n_imgs * img_size + start_range
    pixel_range = np.arange(start_range, end_range, img_size)
    sample_range_x = np.round(z_grid_1, 1)
    sample_range_y = np.round(z_grid_2, 1)
    # 生成画像の表示
    plt.figure(figsize=(10, 10))
    plt.imshow(figure_data)
    plt.xticks(pixel_range, sample_range_x)
    plt.yticks(pixel_range, sample_range_y)
    plt.xlabel("z[0]")
    plt.ylabel("z[1]")
    plt.gray()
    plt.savefig("result.png")
    plt.show()


if __name__ == "__main__":
    main()
