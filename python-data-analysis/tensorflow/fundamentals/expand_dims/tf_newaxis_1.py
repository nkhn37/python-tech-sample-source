"""Tensorの軸を拡張する方法
tf.newaxis 例1

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-expand-dims/#1
"""
import tensorflow as tf

tensor = tf.constant([1, 2, 3, 4, 5], dtype=tf.float16)
print(tensor, "\n")

# ===== Tensorの軸を拡張する tf.newaxis
# 先頭に軸を追加する
expanded_tensor_1 = tensor[tf.newaxis, :]
print(expanded_tensor_1, "\n")

# 末尾に軸を追加する
expanded_tensor_2 = tensor[:, tf.newaxis]
print(expanded_tensor_2)
