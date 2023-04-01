"""文字列基礎
文字列を特定の区切り文字で分割する方法
後方から分割する rsplit

[説明ページ]
https://tech.nkhn37.net/python-split-splitlines-partition/#_rsplit
"""
sample_text1 = "Python Java C C++ C# Go"
sample_text2 = "Python|Java|C|C++|C#|Go"

# ===== 後方から分割する rsplit
# 空白文字で分割
print("--- 空白で分割")
print(sample_text1.rsplit())

# 指定文字で分割
print("--- 指定文字で分割")
print(sample_text2.rsplit("|"))
