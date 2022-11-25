"""RNN(リカレントニューラルネットワーク)による時系列データ予測
実装例

[説明ページ]
https://tech.nkhn37.net/tensorflow-keras-simple-rnn/#TensorFlowKerasRNN
"""
import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers


def main():
    """メイン関数"""
    np.random.seed(1)

    # ===== データ準備
    data_len = 1000
    t = np.arange(data_len)
    y = np.sin(20 * np.pi * t / data_len)
    noise = 0.1 * np.random.randn(data_len)
    input_data = y + noise

    # データを訓練用、評価用、テスト用に分割する
    num_train_samples = int(0.5 * input_data.shape[0])
    num_val_samples = int(0.25 * input_data.shape[0])
    num_test_samples = int(0.25 * input_data.shape[0])
    print(num_train_samples, num_val_samples, num_test_samples)

    # データを描画する
    plt.plot(t, input_data, "b", label="data")
    plt.plot(t, y, "r", label="true")
    plt.legend()
    plt.show()

    # ===== データセットを作成する
    # データのサンプリング、シーケンス、バッチサイズの設定
    sampling_rate = 1
    sequence_length = 100
    sequence_stride = 1
    batch_size = 32

    # 訓練用データセット
    x_train = input_data[0:num_train_samples]
    y_train = y[sampling_rate * sequence_length :]
    train_dataset = keras.utils.timeseries_dataset_from_array(
        x_train,
        targets=y_train,
        sampling_rate=sampling_rate,
        sequence_length=sequence_length,
        sequence_stride=sequence_stride,
        shuffle=True,
        batch_size=batch_size,
    )
    # 評価用データセット
    x_val = input_data[num_train_samples : num_train_samples + num_test_samples]
    y_val = y[num_train_samples + sampling_rate * sequence_length :]
    val_dataset = keras.utils.timeseries_dataset_from_array(
        x_val,
        targets=y_val,
        sampling_rate=sampling_rate,
        sequence_length=sequence_length,
        sequence_stride=sequence_stride,
        shuffle=True,
        batch_size=batch_size,
    )
    # テスト用データセット
    x_test = input_data[num_train_samples + num_val_samples :]
    y_test = y[num_train_samples + num_val_samples + sampling_rate * sequence_length :]
    test_dataset = keras.utils.timeseries_dataset_from_array(
        x_test,
        targets=y_test,
        sampling_rate=sampling_rate,
        sequence_length=sequence_length,
        sequence_stride=sequence_stride,
        shuffle=False,
        batch_size=batch_size,
    )

    # ===== SimpleRNNのモデルを構築する
    inputs = keras.Input(shape=(sequence_length, 1))
    x = layers.SimpleRNN(16, return_sequences=False)(inputs)
    outputs = layers.Dense(1)(x)

    # ===== モデルを構築する
    model = keras.Model(inputs, outputs)

    # ===== オプティマイザ、損失関数、指標を設定してコンパイル
    model.compile(optimizer="adam", loss="mse", metrics=["mae"])
    print(model.summary())

    # ===== モデルの訓練
    epochs = 50
    callbacks = [
        keras.callbacks.ModelCheckpoint("simple_rnn.keras", save_best_only=True)
    ]
    # 訓練の実行
    history = model.fit(
        train_dataset, epochs=epochs, validation_data=val_dataset, callbacks=callbacks
    )

    # ===== history情報の可視化
    # 誤差(Mean Absolute Error)の履歴
    mae = history.history["mae"]
    val_mae = history.history["val_mae"]
    # 誤差履歴描画
    x_epoch = range(1, epochs + 1)
    plt.plot(x_epoch, mae, "r", label="training mae")
    plt.plot(x_epoch, val_mae, "b", label="validation mae")
    plt.xlabel("Epochs")
    plt.ylabel("Mean Absolute Error")
    plt.legend()

    # ===== evaluateを使ったテストデータでの評価
    model = keras.models.load_model("simple_rnn.keras")
    result = model.evaluate(test_dataset)
    print(result)

    # ===== predictを使って予測
    preds = model.predict(test_dataset)
    plt.figure()
    test_start_idx = num_train_samples + num_val_samples
    plt.plot(t[test_start_idx:], input_data[test_start_idx:], "b", label="data")
    plt.plot(t[test_start_idx:], y[test_start_idx:], "r", label="true")
    plt.plot(
        t[test_start_idx + sampling_rate * sequence_length :],
        preds,
        "g",
        label="prediction",
    )
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
