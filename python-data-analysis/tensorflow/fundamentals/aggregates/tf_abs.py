"""集約関数を用いたTensorの集計
絶対値(tf.abs)

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-aggregates/#_tfabs
"""
import tensorflow as tf

tensor = tf.constant([-1, -2, 3, 4, -5])

# 絶対値を計算する tf.abs
abs_tensor = tf.abs(tensor)
print(abs_tensor)
