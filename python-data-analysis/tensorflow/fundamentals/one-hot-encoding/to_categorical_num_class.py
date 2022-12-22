"""one-hotエンコーディングの方法
tf.keras.utils.to_categorical

[説明ページ]
https://tech.nkhn37.net/tensorflow-one-hot-encoding/#num_classes
"""
import tensorflow as tf

labels = tf.constant([2, 1, 3, 1, 0])
num_class = 5

# one-hotエンコーディング tf.keras.utils.to_categorical
# (num_classesによるクラス数の指定)
one_hot_array = tf.keras.utils.to_categorical(labels, num_classes=num_class)
print(one_hot_array)
print(type(one_hot_array))
