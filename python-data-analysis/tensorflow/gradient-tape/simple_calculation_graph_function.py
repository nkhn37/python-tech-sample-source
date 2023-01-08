"""GradientTapeの自動微分による計算方法
具体例：簡単な計算グラフの問題
(フォワード計算は関数化することも可能)

[説明ページ]
https://tech.nkhn37.net/tensorflow-gradienttape/#i-3
"""
import tensorflow as tf


@tf.function
def calc_payment(apple, apple_num, orange, orange_num, tax):
    return tax * (apple * apple_num + orange * orange_num)


def main():
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
        payment = calc_payment(apple, apple_num, orange, orange_num, tax)
    print(f"合計: {payment}", "\n")

    # 勾配計算（リバースモード）
    grads = tape.gradient(payment, [apple, apple_num, orange, orange_num, tax])
    for grad in grads:
        print(grad)


if __name__ == "__main__":
    main()
