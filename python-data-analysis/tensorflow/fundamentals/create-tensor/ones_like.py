"""Tensor(テンソル)の作成方法
1埋めのTensorを作成する方法
既存のTensorと同じ形状で作成する方法: tf.ones_like

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-create-basic/#Tensor_tfones_like
"""
import tensorflow as tf

# ===== 既存のTensorと同じ形状の1埋めTensorを作成する
# 階数1のTensor (vector)
vector = tf.constant([1, 2, 3, 4, 5], dtype=tf.float16)
ones_vector = tf.ones_like(vector)
print(ones_vector, "\n")

# 階数2のTensor (matrix)
matrix = tf.constant([[1, 2], [3, 4]], dtype=tf.float16)
ones_matrix = tf.ones_like(matrix)
print(ones_matrix)
