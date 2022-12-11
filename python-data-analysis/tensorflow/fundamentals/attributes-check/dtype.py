"""Tensor情報の確認方法
Tensorの方を確認する dtype

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-attributes-check/#Tensor_dtype
"""
import tensorflow as tf

tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Tensorの型を確認する dtype
print(tensor, "\n")
print(tensor.dtype)
