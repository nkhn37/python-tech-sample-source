"""Tensorの要素を参照する方法
スライスでTensorの一部を取り出す方法(階数1の場合)

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-access/#1Tensor
"""
import tensorflow as tf

tensor = tf.range(10)
print(tensor, "\n")

# スライスで要素の一部を取り出す
print("スライスで要素の一部を取り出す")
print(f"tensor[2:8] = {tensor[2:8]}")
print(f"tensor[5:] = {tensor[5:]}")
print(f"tensor[:5] = {tensor[:5]}", "\n")

# stepを指定して値を取り出す
print("stepを指定して一定間隔で値を取り出す")
print(f"tensor[0:5:2] = {tensor[0:5:2]}")
print(f"tensor[::2] = {tensor[::2]}", "\n")

# 逆順で値を取り出す
print("逆順で値を取り出す")
print(f"tensor[::-1] = {tensor[::-1]}")
