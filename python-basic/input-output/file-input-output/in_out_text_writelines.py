"""入出力基礎
テキストファイルの書き込み（write）
文字列リストをまとめて書き込む場合

[説明ページ]
https://tech.nkhn37.net/python-open-write/#_writelines
"""
data = [
    "Python\n",
    "ファイルの入出力の基本\n",
    "テキストファイルの入出力",
]

# テキストファイルの書き込み
with open("sample_text_out_list.txt", "w+", encoding="utf-8") as file:
    file.writelines(data)
