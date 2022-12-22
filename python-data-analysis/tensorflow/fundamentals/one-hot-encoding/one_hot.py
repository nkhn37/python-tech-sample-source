"""one-hotエンコーディングの方法
tf.one-hot

[説明ページ]
https://tech.nkhn37.net/tensorflow-one-hot-encoding/#i
"""
import tensorflow as tf

labels = tf.constant([2, 1, 3, 1, 0])
depth = 5

# one-hotエンコーディング tf.one_hot
one_hot_tensor = tf.one_hot(labels, depth)
print(one_hot_tensor)
