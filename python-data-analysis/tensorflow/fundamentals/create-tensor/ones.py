"""Tensor(テンソル)の作成方法
1埋めのTensorを作成する方法
形状を指定して作成する方法: tf.ones

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-create-basic/#_tfones
"""
import tensorflow as tf

# 1埋めのTensorを作成する tf.ones
ones_tensor = tf.ones(shape=(3, 5))
print(ones_tensor)
