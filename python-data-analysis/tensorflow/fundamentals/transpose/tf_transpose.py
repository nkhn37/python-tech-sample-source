"""Tensorを転置する方法
tf.transpose

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-transpose/#tftransposeTensor
"""
import tensorflow as tf

tensor = tf.constant([[1, 2], [3, 4], [5, 6]], dtype=tf.float16)
print(tensor, "\n")

# ===== Tensorを転置する
transposed_tensor = tf.transpose(tensor)
print(transposed_tensor)
