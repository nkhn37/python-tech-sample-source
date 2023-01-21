"""リスト基礎
リスト内包表記を使用しない場合の記載（複数リストから新しいリストを作成）
（リスト内包表記版はlist_complehention_multi.pyを参照）

リスト内包表記は記載がシンプルになるだけではなく、速度も高速なことから
同じ書き方ができる場合は、リスト内包表記を利用することを検討しましょう。

[説明ページ]
https://tech.nkhn37.net/python-list-comprehension/#i-6

[内包表記まとめページ]
https://tech.nkhn37.net/python-comprehension/
"""
# リスト内包表記を使用しない場合の記載方法
data1 = [1, 2, 3, 4, 5]
data2 = [11, 12, 13, 14, 15]
new_data = []

for i in data1:
    if i % 2 == 0:
        for j in data2:
            if j % 2 == 0:
                new_data.append(i * j)
print(f"new_data: {new_data}")
