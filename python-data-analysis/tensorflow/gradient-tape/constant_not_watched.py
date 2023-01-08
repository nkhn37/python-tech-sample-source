"""GradientTapeの自動微分による計算方法
定数Tensorは追跡されない

[説明ページ]
https://tech.nkhn37.net/tensorflow-gradienttape/#Tensor-2
"""
import tensorflow as tf

x = tf.constant(5.0)

# フォワード計算
with tf.GradientTape() as tape:
    result = tf.square(x)
# リバースモードの自動微分を計算（定数だと追跡されない）
gradient = tape.gradient(result, x)

print(gradient)
