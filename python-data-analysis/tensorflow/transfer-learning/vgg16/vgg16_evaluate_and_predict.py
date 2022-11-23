"""保存したモデルを読み込み＆評価＆予測

[説明ページ]
https://tech.nkhn37.net/tensorflow-keras-transfer-learning-vgg16/#i-2
"""
import numpy as np
from tensorflow import keras
from tensorflow.keras.datasets import cifar10


def main():
    _, (test_imgs, test_labels) = cifar10.load_data()

    model = keras.models.load_model("vgg16_cifar10.keras")

    # ===== evaluateを使ったテストデータでの評価
    result = model.evaluate(test_imgs, test_labels)
    print(result)

    # ===== predictを使って予測結果を表示
    preds = model.predict(test_imgs)
    print(f"予測: {np.argmax(preds[0])}, 正解: {test_labels[0]}")


if __name__ == "__main__":
    main()
