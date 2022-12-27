"""集約関数を用いたTensorの集計
総乗(tf.reduce_prod)

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-aggregates/#_tfreduce_prod
"""
import tensorflow as tf

tensor = tf.range(1, 6)

# 総乗を計算する tf.reduce_prod
prod_tensor = tf.reduce_prod(tensor)
print(prod_tensor)
