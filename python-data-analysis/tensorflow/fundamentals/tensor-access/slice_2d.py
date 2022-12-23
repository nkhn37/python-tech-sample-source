"""Tensorの要素を参照する方法
スライスでTensorの一部を取り出す方法(階数2の場合)

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-access/#2Tensor
"""
import tensorflow as tf

tensor = tf.reshape(tf.range(25), shape=(5, 5))
print(tensor, "\n")

# スライスで要素の一部を取り出す
print("スライスで要素の一部を取り出す")
print(f"tensor[:2, :2] = \n{tensor[:2, :2]}")
print(f"tensor[3:, 3:] = \n{tensor[3:, 3:]}", "\n")

# stepを指定して値を取り出す
print("stepを指定して一定間隔で値を取り出す")
print(f"tensor[::2, ::2] = \n{tensor[::2, ::2]}", "\n")

# 逆順で値を取り出す
print("逆順で値を取り出す")
print(f"tensor[::-1, ::-1] = \n{tensor[::-1, ::-1]}")
