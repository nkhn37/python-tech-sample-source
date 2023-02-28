"""入出力基礎
テキストファイルの読み込み
ファイル内容を1行ずつ取得する（readlines）

[説明ページ]
https://tech.nkhn37.net/python-open-write/#1_readline
"""
# for文で順次取り出す方法
with open("sample_text.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")
