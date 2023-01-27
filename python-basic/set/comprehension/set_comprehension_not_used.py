"""集合基礎
集合内包表記を使用しない場合の方法
（集合内包表記版はset_comprehension.pyを参照）

集合内包表記は記載がシンプルになるだけではなく、速度も高速なことから
同じ書き方ができる場合は、集合内包表記を利用することを検討しましょう。

[説明ページ]
https://tech.nkhn37.net/python-set-comprehension/#i-3

[内包表記まとめページ]
https://tech.nkhn37.net/python-comprehension/
"""
data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 10, 15, 20, 25, 30]

# 内包表記を使わない場合
data_set = set()
for dt in data:
    if dt % 2 == 0:
        data_set.add(dt)
print(f"data_set : {data_set}")
