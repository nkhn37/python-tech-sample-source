"""Tensorの軸を拡張する方法
tf.expand_dims 例1

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-expand-dims/#1-2
"""
import tensorflow as tf

tensor = tf.constant([1, 2, 3, 4, 5], dtype=tf.float16)
print(tensor, "\n")

# ===== Tensorの軸を拡張する tf.expand_dims
# 先頭に軸を追加する
expanded_tensor_1 = tf.expand_dims(tensor, axis=0)
print(expanded_tensor_1, "\n")

# 末尾に軸を追加する
expanded_tensor_2 = tf.expand_dims(tensor, axis=-1)
print(expanded_tensor_2)
