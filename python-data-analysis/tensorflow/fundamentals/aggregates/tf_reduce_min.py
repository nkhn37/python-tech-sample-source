"""集約関数を用いたTensorの集計
最小値(tf.reduce_min)

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-aggregates/#_tfreduce_min
"""
import tensorflow as tf

tensor = tf.range(1, 6)

# 最小値を計算する tf.reduce_min
min_tensor = tf.reduce_min(tensor)
print(min_tensor)
