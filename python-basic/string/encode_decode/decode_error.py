"""文字列基礎
バイトを文字列に変換する decodeメソッド (bytes -> str)
文字コードを間違うとエラー (デフォルトでは、errors=strictになっている)

[説明ページ]
https://tech.nkhn37.net/python-encode-decode/#decode
"""
data = "おはようございます。"

# encodeで指定文字コードにエンコードする
encode_data = data.encode("shift_jis")
print(encode_data)

print("================================")
# decodeで文字列に戻す
decode_data = encode_data.decode("utf_8")
print(decode_data)
print(type(decode_data))
