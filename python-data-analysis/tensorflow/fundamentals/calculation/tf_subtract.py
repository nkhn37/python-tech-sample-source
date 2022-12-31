"""Tensorを用いた数値計算
減算 tf.subtract

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-calculation/#_tfsubtract
"""
import tensorflow as tf

a = tf.constant([1, 2, 3, 4, 5])
b = tf.constant([6, 7, 8, 9, 10])
c = tf.constant(2)

# 関数で計算
print(tf.subtract(a, b))
print(tf.subtract(a, c), "\n")

# 演算子で計算
print(a - b)
print(a - c)
