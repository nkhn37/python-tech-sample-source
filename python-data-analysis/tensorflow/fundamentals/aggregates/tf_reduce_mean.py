"""集約関数を用いたTensorの集計
平均(tf.reduce_mean)

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-aggregates/#_tfreduce_mean
"""
import tensorflow as tf

tf.random.set_seed(42)

# 平均5, 標準偏差2の正規分布に従うデータ
tensor = 5 + tf.random.normal(shape=(1000,)) * 2

# 平均値を計算する tf.reduce_mean
mean_tensor = tf.reduce_mean(tensor)
print(mean_tensor)
