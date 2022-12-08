"""Tensor(テンソル)の作成方法
0埋めのTensorを作成する方法
既存のTensorと同じ形状で作成する方法: tf.zeros_like

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-create-basic/#Tensor_tfzeros_like
"""
import tensorflow as tf

# ===== 既存のTensorと同じ形状の0埋めTensorを作成する
# 階数1のTensor (vector)
vector = tf.constant([1, 2, 3, 4, 5], dtype=tf.float16)
zeros_vector = tf.zeros_like(vector)
print(zeros_vector, "\n")

# 階数2のTensor (matrix)
matrix = tf.constant([[1, 2], [3, 4]], dtype=tf.float16)
zeros_matrix = tf.zeros_like(matrix)
print(zeros_matrix)
