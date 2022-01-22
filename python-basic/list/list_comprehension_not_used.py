"""リスト基礎
リスト内包表記を使用しない場合の記載
（リスト内包表記版はlist_complehention.pyを参照）

リスト内包表記は記載がシンプルになるだけではなく、速度も高速なことから
同じ書き方ができる場合は、リスト内包表記を利用することを検討しましょう。

[説明ページ]
https://tech.nkhn37.net/python-list-comprehension/#i

[内包表記まとめページ]
https://tech.nkhn37.net/python-comprehension/
"""
# 普通に記載する方法
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_data = []

for i in data:
    if i % 2 == 0:
        new_data.append(i)
print(f'new_data: {new_data}')
