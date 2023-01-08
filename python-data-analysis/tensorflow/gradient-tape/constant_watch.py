"""GradientTapeの自動微分による計算方法
定数Tensorの追跡方法 tape.watch()

[説明ページ]
https://tech.nkhn37.net/tensorflow-gradienttape/#Tensor_tapewatch
"""
import tensorflow as tf

x = tf.constant(5.0)

# フォワード計算
with tf.GradientTape() as tape:
    # 追跡対象の定数を明確に指定する
    tape.watch(x)
    result = tf.square(x)
# リバースモードの自動微分を計算（定数でも計算できる）
gradient = tape.gradient(result, x)

print(gradient)
