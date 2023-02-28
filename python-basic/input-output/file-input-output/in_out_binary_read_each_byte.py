"""入出力基礎
バイナリファイルの読み込み
ファイル内容を1バイトずつ取得する（read）

[説明ページ]
https://tech.nkhn37.net/python-open-write/#1_read1-2
"""
with open("sample_binary.png", "rb") as file:
    data = []
    while d := file.read(1):
        data.append(d)

print(data, "\n")
data_bin = b"".join(data)
print(data_bin)
