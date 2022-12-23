"""Tensorの要素を参照する方法
単一の要素を参照する方法

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-access/#i
"""
import tensorflow as tf

tensor = tf.range(10)
print(tensor, "\n")

# 単一の要素にアクセスする（インデックスは0から開始）
print(f"tensor[0] = {tensor[0]}")
print(f"tensor[5] = {tensor[5]}")
print(f"tensor[9] = {tensor[9]}")
