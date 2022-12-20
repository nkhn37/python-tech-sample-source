"""Tensorの行列積を計算する方法
tf.matmul
必要に応じて転置して計算

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-matrix-multiplication/#i
"""
import tensorflow as tf

tensor = tf.constant([[1, 2], [3, 4], [5, 6]], dtype=tf.float16)
print(tensor, "\n")

# Tensorの形状に注意　必要に応じて転置をして計算
result = tf.matmul(tensor, tf.transpose(tensor))
print(result, "\n")

result = tf.matmul(tf.transpose(tensor), tensor)
print(result)
