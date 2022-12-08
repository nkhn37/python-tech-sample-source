"""Tensor(テンソル)の作成方法
ランダムな数値でTensorを作成する方法
正規分布に従うTensorを作成する場合: tf.random.normal

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-create-basic/#Tensor_tfrandomnormal
"""
import tensorflow as tf

# 乱数を固定したい場合は、set_seedで設定する
tf.random.set_seed(1)

# 標準正規分布からランダムなTensorを作成する
normal_tensor = tf.random.normal(shape=(3, 5))
print(normal_tensor)
