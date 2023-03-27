"""文字列基礎
スライスで部分文字列を取得する

[説明ページ]
https://tech.nkhn37.net/python-index-slice/#i-3
"""
# スライスで部分文字列を取得する
data = "abcdefghijklmnopqrstuvwxyz"

# start, end, stepを全て指定する
print(data[5:10:2])
# startとendを指定する
print(data[5:10])
# startのみ指定する
print(data[5:])
# endのみ指定する
print(data[:10])
# stepのみ指定する
print(data[::2])

# マイナスの値を指定する
print(data[-5:])
# マイナスの値でstartとendを指定する
print(data[-10:-5])
# stepにマイナスの値を指定する
print(data[::-1])
