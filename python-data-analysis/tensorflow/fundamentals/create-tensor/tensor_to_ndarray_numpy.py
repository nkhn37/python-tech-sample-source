"""Tensor(テンソル)の作成方法
NumPy配列(ndarray)とTensorの相互変換
Tensorをndarrayに変換する方法: numpyメソッド

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-create-basic/#Tensornumpy
"""
import tensorflow as tf

tensor = tf.constant([[1, 2], [3, 4]], dtype=tf.float16)
print(tensor, "\n")

# NumPy配列(ndarray)に変換する numpyメソッド
numpy_array = tensor.numpy()
print(numpy_array)
print(type(numpy_array))
