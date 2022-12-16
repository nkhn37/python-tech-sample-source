"""Tensorの軸を拡張する方法
tf.newaxis 例2

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-expand-dims/#22Tensor
"""
import tensorflow as tf

tensor_2d = tf.constant([[1, 2], [3, 4]], dtype=tf.float16)
print(tensor_2d, "\n")

# ===== Tensorの軸を拡張する tf.newaxis
# 先頭に軸を追加する
expanded_tensor_1 = tensor_2d[tf.newaxis, :, :]
print(expanded_tensor_1, "\n")

# 真ん中に軸を追加する
expanded_tensor_2 = tensor_2d[:, tf.newaxis, :]
print(expanded_tensor_2, "\n")

# 末尾に軸を追加する
expanded_tensor_3 = tensor_2d[:, :, tf.newaxis]
print(expanded_tensor_3)
