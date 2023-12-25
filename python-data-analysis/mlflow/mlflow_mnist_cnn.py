"""MLflowの基本的な使い方
MLflowの使用例のためのサンプルプログラム

[説明ページ]
https://tech.nkhn37.net/mlflow-basic/#MLflow-5
"""
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist

import mlflow
import mlflow.keras


def main():
    """メイン関数"""
    # ===== MLflowの実験設定
    mlflow.set_experiment("mnist_cnn_classification")

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
    # モデル構成の表示
    print(model.summary())
    # # モデルの画像保存
    # keras.utils.plot_model(model, "mnist_cnn_classifier.png", show_shapes=True)

    # モデルのパラメータ設定
    model_optimizer = "adam"
    model_loss = "sparse_categorical_crossentropy"
    # 実行パラメータ設定
    num_epochs = 5
    batch_size = 32

    with mlflow.start_run():
        # モデルパラメータを記録
        mlflow.log_param("optimizer", model_optimizer)
        mlflow.log_param("loss", model_loss)
        # 実行パラメータを登録
        mlflow.log_param("num_epochs", num_epochs)
        mlflow.log_param("batch_size", batch_size)

        # ===== オプティマイザ、損失関数、指標を設定してコンパイル
        model.compile(
            optimizer=model_optimizer,
            loss=model_loss,
            metrics=["accuracy"],
        )

        # ===== fitを使ったモデルの訓練
        history = model.fit(
            train_imgs,
            train_labels,
            epochs=num_epochs,
            batch_size=batch_size,
            validation_data=(val_imgs, val_labels),
        )

        # ===== MLflowにトレーニングのメトリクスを記録
        for epoch in range(num_epochs):
            mlflow.log_metric(
                "loss", history.history["loss"][epoch], step=epoch
            )
            mlflow.log_metric(
                "accuracy", history.history["accuracy"][epoch], step=epoch
            )
            mlflow.log_metric(
                "val_loss", history.history["val_loss"][epoch], step=epoch
            )
            mlflow.log_metric(
                "val_accuracy",
                history.history["val_accuracy"][epoch],
                step=epoch,
            )

        # ===== evaluateを使ったテストデータでの評価
        result = model.evaluate(test_imgs, test_labels)
        print(result)

        # ===== predictを使って予測結果を表示
        pred = model.predict(test_imgs)
        print(f"予測: {np.argmax(pred[0])}, 正解: {test_labels[0]}")

        # ===== MLflowにモデルを記録
        # モデルを保存する
        mlflow.keras.log_model(model, "model")


if __name__ == "__main__":
    main()
