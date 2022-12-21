"""Tensorの形状でサイズ1の次元を削除する方法
tf.squeeze
使用場面例:maeの計算 (tf.squeezeを使用した対応)

[説明ページ]
https://tech.nkhn37.net/tensorflow-tensor-squeeze/#tfsqueeze-2
"""
import tensorflow as tf

# 正解値
y_true = tf.constant([70, 74, 78, 82, 86, 90, 94, 98, 102, 106], dtype=tf.float16)
# 予測値
y_pred = tf.constant(
    [
        70.32939,
        74.9041,
        79.47879,
        84.05348,
        88.628174,
        93.202866,
        97.77756,
        102.35226,
        106.92695,
        111.50165,
    ],
    shape=(10, 1),
    dtype=tf.float16,
)

# mae (mean absolute error)を計算する (squeezeで形状を揃える)
mae = tf.keras.metrics.mean_absolute_error(y_true, tf.squeeze(y_pred))
print(mae)
