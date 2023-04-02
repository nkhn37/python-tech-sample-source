"""文字列基礎
文字列と数値を連結・結合する方法 (+, +=演算子, str, format等)

[説明ページ]
https://tech.nkhn37.net/python-str-join/#i-4
"""
s1 = "a"
n1 = 100

# +演算子で文字列と数値を連結・結合する
temp_str = s1 + "_" + str(n1)
print(temp_str)

# +=演算子で文字列を連結・結合する
n2 = 0.01
temp_str += "_"
temp_str += str(n2)
print(temp_str)

# formatを使用して連結・結合する
temp_str = "{}_{}".format(s1, n1)
print(temp_str)

# f-stringを使用して連結・結合する
temp_str = f"{s1}_{n1:05}_{n2:.5f}"
print(temp_str)
