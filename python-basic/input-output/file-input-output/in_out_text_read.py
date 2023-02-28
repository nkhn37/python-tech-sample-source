"""入出力基礎
テキストファイルの読み込み
ファイル内容をまとめて取得する（read）

[説明ページ]
https://tech.nkhn37.net/python-open-write/#_read
"""
with open("sample_text.txt", "r", encoding="utf-8") as file:
    data = file.read()

print(data)
