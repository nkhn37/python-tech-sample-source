"""Tensor(テンソル)の作成方法
NumPy配列(ndarray)とTensorの相互変換
Tensorをndarrayに変換する方法: np.array関数

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-create-basic/#NumPynparray
"""
import numpy as np
import tensorflow as tf

tensor = tf.constant([[1, 2], [3, 4]], dtype=tf.float16)
print(tensor, "\n")

# NumPy配列(ndarray)に変換する np.arrayを使用
numpy_array = np.array(tensor)
print(numpy_array)
print(type(numpy_array))
