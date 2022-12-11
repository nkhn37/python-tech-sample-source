"""Tensor情報の確認方法
Tensorの形状を確認する shape

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-attributes-check/#Tensor_shape
"""
import tensorflow as tf

tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Tensorの形状を確認する shape
print(tensor, "\n")
print(tensor.shape)
