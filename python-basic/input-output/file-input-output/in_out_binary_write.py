"""入出力基礎
バイナリファイルの書き込み（write）

[説明ページ]
https://tech.nkhn37.net/python-open-write/#_write-2
"""
with open("sample_binary.png", "rb") as file:
    data = file.read()

# バイナリファイルの書き込み
with open("sample_binary_out.png", "wb") as file:
    file.write(data)
