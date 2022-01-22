"""リスト基礎
リスト内包表記の使い方

[説明ページ]
https://tech.nkhn37.net/python-list-comprehension/#i

[内包表記まとめページ]
https://tech.nkhn37.net/python-comprehension/
"""
# dataの中で、2で割り切れる数値のみを取り出してnew_dataを作成する。
# リスト内包表記を使って記載する方法
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_data = [i for i in data if i % 2 == 0]
print(f'new_data: {new_data}')
