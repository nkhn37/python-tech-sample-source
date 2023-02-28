"""入出力基礎
テキストファイルの書き込み（write）

[説明ページ]
https://tech.nkhn37.net/python-open-write/#_write
"""
data = "Python\nファイルの入出力の基本\nテキストファイルの入出力"

# テキストファイルの書き込み
with open("sample_text_out_str.txt", "w+", encoding="utf-8") as file:
    file.write(data)
