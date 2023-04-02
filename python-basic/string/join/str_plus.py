"""文字列基礎
文字列を連結・結合する方法 (+, +=演算子, 文字列リテラル列挙)

[説明ページ]
https://tech.nkhn37.net/python-str-join/#i-3
"""
s1 = "a"
s2 = "b"
s3 = "c"

# +演算子で文字列を連結・結合する
temp_str = s1 + s2 + s3
print(temp_str)

# +=演算子で文字列を連結・結合する
s4 = "d"
temp_str += s4
print(temp_str)

# 文字列リテラルを連続して列挙して連結・結合する
temp_str = "e" "f" "g"
print(temp_str)
