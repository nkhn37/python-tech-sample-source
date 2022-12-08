"""Tensor(テンソル)の作成方法
NumPy配列(ndarray)とTensorの相互変換
ndarrayからTensorを作成する方法

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-create-basic/#NumPyndarrayTensor-2
"""
import numpy as np
import tensorflow as tf

numpy_array = np.arange(1, 11)
print(numpy_array, "\n")

# ===== ndarrayからTensorを作成する
# ndarrayの形状でTensorに変換する
same_shape_tensor = tf.constant(numpy_array)
print(same_shape_tensor, "\n")

# 形状(shape)を指定して変換してTensorを作成する
changed_tensor = tf.constant(numpy_array, shape=(2, 5))
print(changed_tensor)
