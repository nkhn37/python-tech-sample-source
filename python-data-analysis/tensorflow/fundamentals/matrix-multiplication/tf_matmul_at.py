"""Tensorの行列積を計算する方法
tf.matmul
@演算子によるtf.matmulの実行

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-matrix-multiplication/#tfmatmul-3
"""
import tensorflow as tf

tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=tf.float16)
print(tensor, "\n")

# Tensor同士の行列積を計算する @演算子
result = tensor @ tensor
print(result)
