"""集約関数を用いたTensorの集計
最大要素位置(tf.argmax)

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-aggregates/#_tfargmax
"""
import tensorflow as tf

tensor = tf.range(1, 6)

# 最大値の位置を計算する tf.argmax
argmax_tensor = tf.argmax(tensor)
print(argmax_tensor, "\n")

# 最大値を取得する
max_tensor = tensor[argmax_tensor]
print(max_tensor)
