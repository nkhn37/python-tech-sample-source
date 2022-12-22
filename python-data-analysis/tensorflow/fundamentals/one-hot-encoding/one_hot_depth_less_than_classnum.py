"""one-hotエンコーディングの方法
tf.one-hot
depthがデータのクラス数より少ない場合

[説明ページ]
https://tech.nkhn37.net/tensorflow-one-hot-encoding/#depth
"""
import tensorflow as tf

labels = tf.constant([2, 1, 3, 1, 0])
depth = 3

# one-hotエンコーディング tf.one_hot
# (depthがデータのクラス数より少ない場合)
one_hot_tensor = tf.one_hot(labels, depth)
print(one_hot_tensor)
