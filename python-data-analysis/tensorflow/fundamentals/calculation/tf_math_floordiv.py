"""Tensorを用いた数値計算
切り捨て除算 tf.math.floordiv

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-calculation/#_tfmathfloordiv
"""
import tensorflow as tf

a = tf.constant([6, 7, 8, 9, 10])
b = tf.constant([1, 2, 3, 4, 5])
c = tf.constant(2)

# 関数で計算
print(tf.math.floordiv(a, b))
print(tf.math.floordiv(a, c), "\n")

# 演算子で計算
print(a // b)
print(a // c)
