"""Tensorを用いた数値計算
マイナス tf.negative

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-calculation/#_tfnegative
"""
import tensorflow as tf

a = tf.constant([1, 2, 3, 4, 5])
b = tf.constant(2)

# 関数で計算
print(tf.negative(a))
print(tf.negative(b), "\n")

# 演算子で計算
print(-a)
print(-b)
