"""集約関数を用いたTensorの集計
最小要素位置(tf.argmin)

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-aggregates/#_tfargmin
"""
import tensorflow as tf

tensor = tf.range(1, 6)

# 最小値の位置を計算する tf.argmin
argmin_tensor = tf.argmin(tensor)
print(argmin_tensor, "\n")

# 最小値を取得する
min_tensor = tensor[argmin_tensor]
print(min_tensor)
