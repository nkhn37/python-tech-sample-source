"""Tensor(テンソル)の作成方法
ランダムな数値でTensorを作成する方法
0~1のランダムなTensorを作成する場合: tf.random.uniform

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-create-basic/#01Tensor_tfrandomuniform
"""
import tensorflow as tf

# 乱数を固定したい場合は、set_seedで設定する
tf.random.set_seed(1)

# 0~1の乱数でTensorを作成する
uniform_tensor = tf.random.uniform(shape=(3, 5))
print(uniform_tensor)
