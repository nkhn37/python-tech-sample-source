"""Tensorの形状を変更する方法
tf.reshape

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-reshape/#Tensor_tfreshape
"""
import numpy as np
import tensorflow as tf

n = 20
tensor = tf.constant(np.arange(1, n + 1), dtype=tf.float16)
print(tensor, "\n")

# ===== Tensorの形状を変更する
# 行ベクトル
reshaped_tensor_1 = tf.reshape(tensor, shape=(1, n))
print(reshaped_tensor_1, "\n")

# 列ベクトル
reshaped_tensor_2 = tf.reshape(tensor, shape=(n, 1))
print(reshaped_tensor_2, "\n")

# 2階のTensorへ変更
reshaped_tensor_3 = tf.reshape(tensor, shape=(5, 4))
print(reshaped_tensor_3, "\n")

# 3階のTensorへ変更
reshaped_tensor_4 = tf.reshape(tensor, shape=(5, 2, 2))
print(reshaped_tensor_4)
