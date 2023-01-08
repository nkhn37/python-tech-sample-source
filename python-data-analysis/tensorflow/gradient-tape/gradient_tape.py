"""GradientTapeの自動微分による計算方法
基本的な使い方

[説明ページ]
https://tech.nkhn37.net/tensorflow-gradienttape/#GradientTape
"""
import tensorflow as tf

x = tf.Variable(5.0)

# フォワード計算
with tf.GradientTape() as tape:
    result = tf.square(x)
# リバースモードの自動微分を計算
gradient = tape.gradient(result, x)

print(gradient)
