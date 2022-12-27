"""集約関数を用いたTensorの集計
分散(tf.math.reduce_variance)
エラーとなる場合

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-aggregates/#i
"""
import tensorflow as tf

tensor = tf.constant([1, 2, 3, 4, 5])

# 分散を計算する tf.math.reduce_variance
var_tensor = tf.math.reduce_variance(tensor)
print(var_tensor)
