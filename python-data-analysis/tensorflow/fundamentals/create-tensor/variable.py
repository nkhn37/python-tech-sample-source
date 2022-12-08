"""Tensor(テンソル)の作成方法
変数Tensorの作成 tf.Variable

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-create-basic/#i-4
"""
import tensorflow as tf

# ===== 変数を作成する tf.Variable
# 階数0のTensor (scalar)
scalar = tf.Variable(10)
print(scalar, "\n")

# 階数1のTensor (vector)
vector = tf.Variable([1, 2, 3, 4, 5])
print(vector, "\n")

# 階数2のTensor (matrix)
matrix_2d = tf.Variable([[1, 2], [3, 4]])
print(matrix_2d, "\n")

# 階数3のTensor (matrix)
matrix_3d = tf.Variable([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
print(matrix_3d, "\n")

# 階数4のTensor (matrix)
matrix_4d = tf.Variable(
    [
        [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]],
        [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]],
    ]
)
print(matrix_4d)
