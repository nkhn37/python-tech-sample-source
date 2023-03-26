"""文字列基礎
lowerより強力に大文字を小文字に変換する casefoldメソッド

[説明ページ]
https://tech.nkhn37.net/python-upper-lower-translation/#lower_casefold
"""
# lowerより強力に大文字を小文字に変換する casefold
data = "Fußball"
print(f"元の文字列: {data}")
print(f"変換後の文字列(casefoldの場合): {data.casefold()}")
print(f"変換後の文字列(lowerの場合): {data.lower()}")
