"""集約関数を用いたTensorの集計
すべての要素がTrue (tf.reduce_all)

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-aggregates/#True_tfreduce_all
"""
import tensorflow as tf

tensor_1 = tf.constant([False, False, False])
tensor_2 = tf.constant([True, False, True])
tensor_3 = tf.constant([True, True, True])

# 全てTrueの場合を判定 tf.reduce_all
print(tf.reduce_all(tensor_1))
print(tf.reduce_all(tensor_2))
print(tf.reduce_all(tensor_3))
