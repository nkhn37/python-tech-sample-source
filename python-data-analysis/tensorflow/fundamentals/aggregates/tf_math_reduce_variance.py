"""集約関数を用いたTensorの集計
分散(tf.math.reduce_variance)

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-aggregates/#_tfmathreduce_variance
"""
import tensorflow as tf

tf.random.set_seed(42)

# 平均5, 標準偏差2の正規分布に従うデータ
tensor = 5 + tf.random.normal(shape=(1000,)) * 2

# 分散を計算する tf.math.reduce_variance
var_tensor = tf.math.reduce_variance(tensor)
print(var_tensor)
