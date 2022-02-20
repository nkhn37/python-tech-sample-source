"""入出力基礎
バイナリファイルの読み込み
ファイル内容を1バイトずつ取得する（read）

[説明ページ]
https://tech.nkhn37.net/python-open-write/#1-3
"""
with open('sample_binary.png', 'rb') as file:
    data = []
    while d := file.read(1):
        data.append(d)

print(data)
data_bin = b''.join(data)
print(data_bin)
