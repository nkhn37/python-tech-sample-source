"""入出力基礎
バイナリファイルの読み込み
ファイル内容をまとめて取得する（read）

[説明ページ]
https://tech.nkhn37.net/python-open-write/#i-6
"""
with open('sample_binary.png', 'rb') as file:
    data = file.read()

print(data)
