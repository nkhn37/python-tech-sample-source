"""Tensorの行列積を計算する方法
tf.matmul
行列積ではTensorの形状に注意

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-matrix-multiplication/#Tensor-2
"""
import tensorflow as tf

tensor = tf.constant([[1, 2], [3, 4], [5, 6]], dtype=tf.float16)
print(tensor, "\n")

# Tensorの形状に注意　以下はエラー
result = tf.matmul(tensor, tensor)
print(result)
