"""入出力基礎
テキストファイルの書き込み（write）

[説明ページ]
https://tech.nkhn37.net/python-open-write/#write
"""
with open('sample_text.txt', 'r', encoding='utf-8') as file:
    data = file.read()

# テキストファイルの書き込み
with open('sample_text_out.txt', 'w+', encoding='utf-8') as file:
    file.write(data)
