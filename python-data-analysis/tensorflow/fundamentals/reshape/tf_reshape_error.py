"""Tensorの形状を変更する方法
tf.reshape
サイズが変更前後で合わないとエラーとなるので注意

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-reshape/#i-2
"""
import numpy as np
import tensorflow as tf

n = 20
tensor = tf.constant(np.arange(1, n + 1), dtype=tf.float16)
print(tensor, "\n")

# Tensorの形状を変更する（サイズが合わないとエラー）
reshaped_tensor = tf.reshape(tensor, shape=(4, 2, 2))
print(reshaped_tensor)
