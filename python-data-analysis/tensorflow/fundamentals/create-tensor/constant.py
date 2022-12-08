"""Tensor(テンソル)の作成方法
定数Tensorの作成 tf.constant

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-create-basic/#i
"""
import tensorflow as tf

# ===== 定数を作成する tf.constant
# 階数0のTensor (scalar)
scalar = tf.constant(10)
print(scalar)
print(scalar.ndim, "\n")

# 階数1のTensor (vector)
vector = tf.constant([1, 2, 3, 4, 5])
print(vector)
print(vector.ndim, "\n")

# 階数2のTensor (matrix)
matrix_2d = tf.constant([[1, 2], [3, 4]])
print(matrix_2d)
print(matrix_2d.ndim, "\n")

# 階数3のTensor (matrix)
matrix_3d = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
print(matrix_3d)
print(matrix_3d.ndim, "\n")

# 階数4のTensor (matrix)
matrix_4d = tf.constant(
    [
        [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]],
        [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]],
    ]
)
print(matrix_4d)
print(matrix_4d.ndim)
