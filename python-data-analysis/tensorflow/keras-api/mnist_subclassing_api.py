"""Keras API
Subclassing APIでのMNIST手書き文字分類 実装例

[説明ページ]
https://tech.nkhn37.net/tensorflow-keras-sequential-functional-subclassing-api/#i-7
"""
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist


class MnistModel(keras.Model):
    """MNIST 分類モデル"""

    def __init__(self):
        """コンストラクタ"""
        # superのコンストラクタを呼び出す
        super(MnistModel, self).__init__()
        # 各層の定義を行う
        self.layer1 = layers.Dense(256, activation="relu")
        self.layer2 = layers.Dense(256, activation="relu")
        self.dropout = layers.Dropout(0.5)
        self.classifier = layers.Dense(10, activation="softmax")

    def call(self, x):
        """フォワード処理

        Args:
            x: 入力データ

        Returns:
            フォワード処理の計算結果
        """
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.dropout(x)
        outputs = self.classifier(x)

        return outputs


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

    # ===== モデルを構築する（Subclassing APIを使用）
    model = MnistModel()

    # ===== optimizer、損失関数、指標を指定してコンパイル
    model.compile(
        optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
    )

    # ===== fitを使ったモデルの訓練
    history = model.fit(
        train_imgs, train_labels, epochs=5, validation_data=(val_imgs, val_labels)
    )

    # ===== evaluateを使ったテストデータでの評価
    result = model.evaluate(test_imgs, test_labels)
    print(result)

    # ===== predictを使って予測結果を表示
    # preds = model(test_imgs)でも同じ
    preds = model.predict(test_imgs)
    print(f"予測: {np.argmax(preds[0])}, 正解: {test_labels[0]}")


if __name__ == "__main__":
    main()
