"""DCGAN(Deep Convolutional GAN)の実装

[説明ページ]
https://tech.nkhn37.net/tensorflow-keras-dcgan/
"""
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.activations import tanh
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Conv2DTranspose
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import LeakyReLU
from tensorflow.keras.layers import Reshape


def mnist_descriminator():
    """Discriminator(識別器)モデルの構築(MMIST用)

    Returns:
        識別器モデル
    """
    # ===== Discriminatorの構築
    # 入力
    inputs = keras.Input(shape=(28, 28, 1))
    # 畳み込み(14×14×64)
    x = Conv2D(64, kernel_size=5, strides=2, padding="same")(inputs)
    x = BatchNormalization()(x)
    x = LeakyReLU()(x)
    # 畳み込み(7×7×128)
    x = Conv2D(128, kernel_size=5, strides=2, padding="same")(x)
    x = BatchNormalization()(x)
    x = LeakyReLU()(x)
    # 全結合層への接続
    x = Flatten()(x)
    x = Dropout(0.3)(x)
    # 識別のための層
    outputs = Dense(1, activation="sigmoid")(x)
    # モデルの生成
    model = keras.Model(inputs=inputs, outputs=outputs, name="mnist_discriminator")

    return model


def mnist_generator(latent_dim=100):
    """Generator(生成器)モデルの構築(MNIST用)

    Args:
        latent_dim: 潜在次元数(デフォルト: 100)

    Returns:
        生成器モデル
    """
    # ===== Generatorの構築
    # 入力
    inputs = keras.Input(shape=(latent_dim,))
    # Discriminatorと同じ数にマッピングし、reshapeする
    x = Dense(7 * 7 * 128)(inputs)
    x = Reshape((7, 7, 128))(x)
    # 逆畳み込み(7×7×128)
    x = Conv2DTranspose(128, kernel_size=5, strides=1, padding="same")(x)
    x = BatchNormalization()(x)
    x = LeakyReLU()(x)
    # 逆畳み込み(14×14×64)
    x = Conv2DTranspose(64, kernel_size=5, strides=2, padding="same")(x)
    x = BatchNormalization()(x)
    x = LeakyReLU()(x)
    # 逆畳み込み(28×28×1)
    x = Conv2DTranspose(1, kernel_size=5, strides=2, padding="same")(x)
    outputs = tanh(x)
    # モデルの生成
    model = keras.Model(inputs=inputs, outputs=outputs, name="mnist_generator")

    return model


class DCGAN(keras.Model):
    """DCGANモデルクラス"""

    def __init__(self, discriminator, generator, latent_dim):
        """コンストラクタ

        Args:
            discriminator: 識別器
            generator: 生成器
            latent_dim: 潜在次元数
        """
        super(DCGAN, self).__init__()
        self.discriminator = discriminator
        self.generator = generator
        self.latent_dim = latent_dim
        # オプティマイザ
        self.d_optimizer = None
        self.g_optimizer = None
        # 損失関数
        self.loss_fn = None
        # 損失値の指標追跡用
        self.d_loss_metric = keras.metrics.Mean(name="d_loss")
        self.g_loss_metric = keras.metrics.Mean(name="g_loss")

    def compile(self, d_optimizer, g_optimizer, loss_fn, **kwargs):
        """コンパイルメソッド

        Args:
            d_optimizer: Discriminator(識別器)のオプティマイザー
            g_optimizer: Generator(生成器)のオプティマイザー
            loss_fn: 損失関数
        """
        super(DCGAN, self).compile(**kwargs)
        self.d_optimizer = d_optimizer
        self.g_optimizer = g_optimizer
        self.loss_fn = loss_fn

    @property
    def metrics(self):
        return [self.d_loss_metric, self.g_loss_metric]

    def discriminator_loss(self, real_output, fake_output):
        """Discriminator(識別器)の損失関数計算

        Args:
            real_output: 正解画像に対する識別結果
            fake_output: 偽物画像に対する識別結果

        Returns:
            Discriminator(識別器)の損失関数の値
        """
        # ===== 計算準備
        # 本物と偽物用のラベル生成(本物1, 偽物0)
        labels = tf.concat(
            [tf.ones_like(real_output), tf.zeros_like(fake_output)], axis=0
        )
        labels += 0.05 * tf.random.uniform(tf.shape(labels))

        # 本物と偽物による識別結果を結合
        output = tf.concat([real_output, fake_output], axis=0)

        # ===== 損失値の計算
        d_loss = self.loss_fn(labels, output)

        return d_loss

    def generator_loss(self, fake_output):
        """Generator(生成器)の損失関数計算

        Args:
            fake_output: 偽物画像に対する識別結果

        Returns:
            Generator(生成器)の損失関数の値
        """
        # 生成画像に対する損失値
        g_loss = self.loss_fn(tf.ones_like(fake_output), fake_output)

        return g_loss

    def train_step(self, real_imgs):
        """DCGANの訓練ステップ

        Args:
            real_imgs: 正解画像

        Returns:
            損失関数の値リスト([識別器, 生成器])
        """
        # バッチサイズを取得
        batch_size = tf.shape(real_imgs)[0]
        # ノイズを生成
        noise_vectors = tf.random.normal(shape=(batch_size, self.latent_dim))
        # Generator(生成器)を使って偽物の画像を生成
        generated_imgs = self.generator(noise_vectors)

        # ===== discriminatorの訓練
        with tf.GradientTape() as d_tape:
            # 正解画像に対する識別
            real_output = self.discriminator(real_imgs, training=True)
            # 偽物画像に対する識別
            fake_output = self.discriminator(generated_imgs, training=True)
            # 識別器の損失関数の値計算
            d_loss = self.discriminator_loss(real_output, fake_output)
        # 勾配計算
        d_grads = d_tape.gradient(d_loss, self.discriminator.trainable_weights)
        # 重みの更新
        self.d_optimizer.apply_gradients(
            zip(d_grads, self.discriminator.trainable_weights)
        )

        # ===== generatorの訓練
        with tf.GradientTape() as g_tape:
            # 偽物画像に対する識別
            fake_output = self.discriminator(
                self.generator(noise_vectors), training=True
            )
            # 生成器の損失関数の値計算
            g_loss = self.generator_loss(fake_output)
        # 勾配計算
        g_grads = g_tape.gradient(g_loss, self.generator.trainable_weights)
        # 重みの更新
        self.g_optimizer.apply_gradients(zip(g_grads, self.generator.trainable_weights))

        # 損失関数の値を更新
        self.d_loss_metric.update_state(d_loss)
        self.g_loss_metric.update_state(g_loss)

        # 損失関数の値の返却
        return {
            "d_loss": self.d_loss_metric.result(),
            "g_loss": self.g_loss_metric.result(),
        }


class GanMonitor(keras.callbacks.Callback):
    """GANの結果画像をエポックの終了時に保存するコールバッククラス"""

    def __init__(self, latent_dim=100):
        """コンストラクタ

        Args:
            latent_dim: 潜在次元数(デフォルト: 100)
        """
        # 生成画像数
        self.num_imgs = 25
        # 潜在次元数
        self.latent_dim = latent_dim
        # 生成の元となるノイズの生成
        self.noise_vectors = tf.random.normal(shape=(self.num_imgs, self.latent_dim))

    def on_epoch_end(self, epoch, logs):
        """エポック終了時実行メソッド

        Args:
            epoch: エポック数
            logs: ログ
        """
        # ノイズから偽物画像を生成
        generated_imgs = self.model.generator(self.noise_vectors, training=False)
        # 元のスケールに修正
        generated_imgs = generated_imgs * 127.5 + 127.5

        # 画像を表示
        fig = plt.figure(figsize=(5, 5))
        for i in range(generated_imgs.shape[0]):
            plt.subplot(5, 5, i + 1)
            plt.imshow(generated_imgs[i, :, :, 0], cmap="gray")
            plt.axis("off")
        fig.suptitle(f"Epoch: {epoch + 1:04d}")
        plt.savefig(f"generated_imgs_{epoch + 1:04d}.png")


def main():
    """メイン関数"""
    # ===== MNIST(エムニスト)データの読込
    (train_imgs, _), (test_imgs, _) = mnist.load_data()
    # 全ての画像を使って生成モデルを訓練するため訓練データとテストデータを結合
    train_imgs = np.concatenate([train_imgs, test_imgs], axis=0)
    # reshape
    train_imgs = train_imgs.reshape((70000, 28, 28, 1)).astype("float32")
    # 正規化(-1~1)
    train_imgs = (train_imgs - 127.5) / 127.5

    # ===== データセットの生成
    buffer_size = 32
    batch_size = 32
    train_dataset = tf.data.Dataset.from_tensor_slices(train_imgs)
    # シャフルしてバッチ化
    train_dataset = train_dataset.shuffle(buffer_size).batch(batch_size)

    # ===== DCGANの構築
    # 潜在次元数
    latent_dim = 100
    # Discriminator(識別器)の生成
    discriminator = mnist_descriminator()
    print(discriminator.summary())
    keras.utils.plot_model(discriminator, "discriminator.png", show_shapes=True)
    # Generator(生成器)の生成
    generator = mnist_generator(latent_dim=latent_dim)
    print(generator.summary())
    keras.utils.plot_model(generator, "generator.png", show_shapes=True)

    # ===== DCGANモデルの構築
    dcgan = DCGAN(discriminator, generator, latent_dim)

    # ===== モデルのコンパイル
    dcgan.compile(
        d_optimizer=keras.optimizers.Adam(1e-5),
        g_optimizer=keras.optimizers.Adam(1e-5),
        loss_fn=keras.losses.BinaryCrossentropy(),
        run_eagerly=True,
    )

    # ===== モデルの学習
    n_epochs = 50
    dcgan.fit(
        train_dataset, epochs=n_epochs, callbacks=[GanMonitor(latent_dim=latent_dim)]
    )


if __name__ == "__main__":
    main()
