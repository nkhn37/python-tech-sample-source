"""Tensor情報の確認方法
Tensorの要素数を確認する tf.size

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-attributes-check/#Tensor_tfsize
"""
import tensorflow as tf

tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Tensorの要素数を確認する tf.size
print(tensor, "\n")
print(tf.size(tensor))
