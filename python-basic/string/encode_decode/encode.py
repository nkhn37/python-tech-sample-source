"""文字列基礎
文字列をバイトに変換する encodeメソッド (str -> bytes)

[説明ページ]
https://tech.nkhn37.net/python-encode-decode/#_encode
"""
data = "おはようございます。"

# encodeで指定文字コードにエンコードする
encode_data = data.encode("shift_jis")
print(encode_data)
print(type(encode_data))
