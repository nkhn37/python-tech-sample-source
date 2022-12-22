"""one-hotエンコーディングの方法
tf.keras.utils.to_categorical

[説明ページ]
https://tech.nkhn37.net/tensorflow-one-hot-encoding/#i-2
"""
import tensorflow as tf

labels = tf.constant([2, 1, 3, 1, 0])

# one-hotエンコーディング tf.keras.utils.to_categorical
one_hot_array = tf.keras.utils.to_categorical(labels)
print(one_hot_array)
print(type(one_hot_array))
