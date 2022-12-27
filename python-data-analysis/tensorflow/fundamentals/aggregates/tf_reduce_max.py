"""集約関数を用いたTensorの集計
最大値(tf.reduce_max)

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-aggregates/#_tfreduce_max
"""
import tensorflow as tf

tensor = tf.range(1, 6)

# 最大値を計算する tf.reduce_max
max_tensor = tf.reduce_max(tensor)
print(max_tensor)
