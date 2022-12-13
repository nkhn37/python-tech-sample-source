"""Tensorのシャッフル方法
tf.random.shuffle

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-shuffle/#Tensor_tfrandomshuffle
"""
import numpy as np
import tensorflow as tf

tensor = tf.constant(np.arange(1, 51), shape=(10, 5))
print(tensor, "\n")

# グローバルな乱数シードの設定
tf.random.set_seed(0)

# Tensorをシャッフルする (オペレーションの乱数シードの設定)
shuffled_tensor = tf.random.shuffle(tensor, seed=1)
print(shuffled_tensor)
