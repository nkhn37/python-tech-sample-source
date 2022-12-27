"""集約関数を用いたTensorの集計
標準偏差(tf.math.reduce_std)
エラーとなる場合

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-aggregates/#i-2
"""
import tensorflow as tf

tensor = tf.constant([1, 2, 3, 4, 5])

# 標準偏差を計算する tf.math.reduce_std
std_tensor = tf.math.reduce_std(tensor)
print(std_tensor)
