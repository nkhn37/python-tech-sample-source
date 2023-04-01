"""文字列基礎
文字列を特定の区切り文字で分割する方法
前方から分割する split

[説明ページ]
https://tech.nkhn37.net/python-split-splitlines-partition/#_split
"""
sample_text1 = "Python Java C C++ C# Go"
sample_text2 = "Python|Java|C|C++|C#|Go"

# ===== 前方から分割する split
# 空白文字で分割
print("--- 空白で分割")
print(sample_text1.split())

# 指定文字で分割
print("--- 指定文字で分割")
print(sample_text2.split("|"))
