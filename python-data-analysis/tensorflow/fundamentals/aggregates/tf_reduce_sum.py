"""集約関数を用いたTensorの集計
総和(tf.reduce_sum)

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-aggregates/#_tfreduce_sum
"""
import tensorflow as tf

tensor = tf.range(1, 6)

# 総和を計算する tf.reduce_sum
sum_tensor = tf.reduce_sum(tensor)
print(sum_tensor)
