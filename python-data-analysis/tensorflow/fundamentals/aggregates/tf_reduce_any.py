"""集約関数を用いたTensorの集計
いずれかの要素がTrue (tf.reduce_any)

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-aggregates/#True_tfreduce_any
"""
import tensorflow as tf

tensor_1 = tf.constant([False, False, False])
tensor_2 = tf.constant([True, False, True])
tensor_3 = tf.constant([True, True, True])

# いずれかがTrueの場合を判定 tf.reduce_any
print(tf.reduce_any(tensor_1))
print(tf.reduce_any(tensor_2))
print(tf.reduce_any(tensor_3))
