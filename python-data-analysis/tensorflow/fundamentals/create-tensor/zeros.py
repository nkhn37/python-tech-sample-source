"""Tensor(テンソル)の作成方法
0埋めのTensorを作成する方法
形状を指定して作成する方法: tf.zeros

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-create-basic/#_tfzeros
"""
import tensorflow as tf

# 0埋めのTensorを作成する tf.zeros
zeros_tensor = tf.zeros(shape=(3, 5))
print(zeros_tensor)
