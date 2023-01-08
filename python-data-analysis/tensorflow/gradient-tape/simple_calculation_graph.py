"""GradientTapeの自動微分による計算方法
具体例：簡単な計算グラフの問題

[説明ページ]
https://tech.nkhn37.net/tensorflow-gradienttape/#i
"""
import tensorflow as tf

# りんごの価格
apple = tf.Variable(100.0)
# りんごの個数
apple_num = tf.Variable(2.0)
# みかんの価格
orange = tf.Variable(150.0)
# みかんの個数
orange_num = tf.Variable(3.0)
# 消費税
tax = tf.Variable(1.1)

# フォワード計算
with tf.GradientTape() as tape:
    apple_val = apple * apple_num
    orange_val = orange * orange_num
    sum_val = apple_val + orange_val
    payment = tax * sum_val
print(f"支払金額: {payment}", "\n")

# 勾配計算（リバースモード）
grads = tape.gradient(payment, [apple, apple_num, orange, orange_num, tax])
for grad in grads:
    print(grad)
