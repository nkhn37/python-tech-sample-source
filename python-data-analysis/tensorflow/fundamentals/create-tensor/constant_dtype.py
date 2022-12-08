"""Tensor(テンソル)の作成方法
tf.constantで型を指定して作成する

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-create-basic/#i-2
"""
import tensorflow as tf

# dtypeで型を指定して定数を作成する tf.constant
matrix = tf.constant([[1, 2], [3, 4]], dtype=tf.float16)
print(matrix)
