"""型ヒント（変数・関数の型アノテーション）の基本
型エイリアス

[説明ページ]
https://tech.nkhn37.net/python-type-annotation-basic/#i-5
"""
# 型エイリアスの作成
Vector = list[float]

new_vector: Vector = [1.0, 2, 0, 3.0]
print(new_vector)
