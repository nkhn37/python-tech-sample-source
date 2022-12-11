"""Tensor情報の確認方法
Tensorの階数を確認する ndim

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-attributes-check/#Tensor_ndim
"""
import tensorflow as tf

tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Tensorの次元数を確認する ndim
print(tensor, "\n")
print(tensor.ndim)
