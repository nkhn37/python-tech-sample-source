"""Tensor(テンソル)の作成方法
tf.constantにはtf.Variableにあるassignは存在しない

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-create-basic/#assigntfconstant
"""
import tensorflow as tf

tensor = tf.constant([[1, 2], [3, 4]], dtype=tf.float16)

# tf.constantにはtf.Variableにあるassignは存在しない (AttributeError)
tensor[0, 0].assign(5)
print(tensor)
