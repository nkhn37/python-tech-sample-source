"""Tensorの形状でサイズ1の次元を削除する方法
tf.squeeze

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-squeeze/#tfsqueeze1
"""
import tensorflow as tf

tf.random.set_seed(42)
tensor = tf.constant(tf.random.uniform(shape=(10,)), shape=(1, 1, 1, 1, 10))
print(tensor, "\n")

# サイズが1の次元を削除する tf.squeeze
squeezed_tensor = tf.squeeze(tensor)
print(squeezed_tensor)
