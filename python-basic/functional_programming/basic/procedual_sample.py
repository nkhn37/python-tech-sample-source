"""Pythonを用いた関数型プログラミング
関数型との比較のための手続き型の書き方例

[説明ページ]
https://tech.nkhn37.net/python-functional-programming/#i-4
"""
target = [1, 2, 3, 4, 5]

# 手続きで書く場合
sum_value = 0
for d in target:
    sum_value += d**2
print(sum_value)
