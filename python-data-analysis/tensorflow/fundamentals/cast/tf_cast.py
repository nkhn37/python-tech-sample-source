"""Tensorの型変換方法
tf.cast

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-cast/#Tensor_tfcast
"""
import tensorflow as tf

tensor = tf.constant([1, 2, 3, 4, 5])
print(tensor, "\n")

# Tensorの型を変換する
tensor_float16 = tf.cast(tensor, dtype=tf.float16)
print(tensor_float16)
tensor_float32 = tf.cast(tensor, dtype=tf.float32)
print(tensor_float32)
tensor_float64 = tf.cast(tensor, dtype=tf.float64)
print(tensor_float64)
