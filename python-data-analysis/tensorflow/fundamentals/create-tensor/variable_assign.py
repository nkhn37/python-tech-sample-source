"""Tensor(テンソル)の作成方法
tf.Variableの変数の値を変更する方法 assign

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-create-basic/#_assign
"""
import tensorflow as tf

tensor = tf.Variable([[1, 2], [3, 4]], dtype=tf.float16)

# Tensorの値を更新する assign
tensor[0, 0].assign(5)
print(tensor)
