"""Tensorの軸を拡張する方法
tf.expand_dims 例2

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-expand-dims/#22Tensor-2
"""
import tensorflow as tf

tensor_2d = tf.constant([[1, 2], [3, 4]], dtype=tf.float16)
print(tensor_2d, "\n")

# ===== Tensorの軸を拡張する tf.expand_dims
# 先頭に軸を追加する
expanded_tensor_1 = tf.expand_dims(tensor_2d, axis=0)
print(expanded_tensor_1, "\n")

# 真ん中に軸を追加する
expanded_tensor_2 = tf.expand_dims(tensor_2d, axis=1)
print(expanded_tensor_2, "\n")

# 末尾に軸を追加する
expanded_tensor_3 = tf.expand_dims(tensor_2d, axis=-1)
print(expanded_tensor_3)
