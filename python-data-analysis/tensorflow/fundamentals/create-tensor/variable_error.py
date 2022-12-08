"""Tensor(テンソル)の作成方法
tf.Variableは直接変更しようとするとTypeErrorとなる

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-create-basic/#_assign
"""
import tensorflow as tf

tensor = tf.Variable([[1, 2], [3, 4]], dtype=tf.float16)

# 変数は直接は変更できない (TypeError)
tensor[0, 0] = 5
