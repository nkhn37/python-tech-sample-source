"""one-hotエンコーディングの方法
tf.one-hot
on_value, off_valueによる値の指定

[説明ページ]
https://tech.nkhn37.net/tensorflow-one-hot-encoding/#on_value_off_value
"""
import tensorflow as tf

labels = tf.constant([2, 1, 3, 1, 0])
depth = 5

# one-hotエンコーディング tf.one_hot
# (on_value, off_valueの指定)
one_hot_tensor = tf.one_hot(labels, depth, on_value=5.0, off_value=-1.0)
print(one_hot_tensor)
