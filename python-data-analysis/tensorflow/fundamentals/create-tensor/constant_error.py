"""Tensor(テンソル)の作成方法
tf.constantの要素の値は変更できない

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-create-basic/#i-3
"""
import tensorflow as tf

tensor = tf.constant([[1, 2], [3, 4]], dtype=tf.float16)

# 定数は変更できない
tensor[0, 0] = 5
print(tensor)
