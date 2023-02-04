"""if文基礎
三項演算子の基本的な使い方
(条件により設定する値や式を切り替える)

[説明ページ]
https://tech.nkhn37.net/python-if-basic/#i-3
"""
# 三項演算子で条件により設定する値を切り替える
num = 1
result = "even" if num % 2 == 0 else "odd"
print(result)

num = 2
result = "even" if num % 2 == 0 else "odd"
print(result)

# 三項演算子で条件により式を切り替える
num = 3
result = num * 2 if num % 2 == 0 else num * 3
print(result)

num = 4
result = num * 2 if num % 2 == 0 else num * 3
print(result)
