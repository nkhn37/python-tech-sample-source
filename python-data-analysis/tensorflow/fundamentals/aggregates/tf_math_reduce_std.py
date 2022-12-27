"""集約関数を用いたTensorの集計
標準偏差(tf.math.reduce_std)

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-aggregates/#_tfmathreduce_std
"""
import tensorflow as tf

tf.random.set_seed(42)

# 平均5, 標準偏差2の正規分布に従うデータ
tensor = 5 + tf.random.normal(shape=(1000,)) * 2

# 標準偏差を計算する tf.math.reduce_std
std_tensor = tf.math.reduce_std(tf.cast(tensor, dtype=tf.float32))
print(std_tensor)
