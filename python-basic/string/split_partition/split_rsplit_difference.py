"""文字列基礎
文字列を特定の区切り文字で分割する方法
splitとrsplitの結果が変わる場合

[説明ページ]
https://tech.nkhn37.net/python-split-splitlines-partition/#splitrsplit
"""
sample_text1 = 'Python Java C C++ C# Go'
sample_text2 = 'Python|Java|C|C++|C#|Go'

# ===== splitとrsplitの分割結果が変わる場合
# 空白文字で分割
print('--- 空白で分割')
print(sample_text1.split(maxsplit=3))
print(sample_text1.rsplit(maxsplit=3))

# 指定文字で分割
print('--- 指定文字で分割')
print(sample_text2.split('|', maxsplit=3))
print(sample_text2.rsplit('|', maxsplit=3))
# # 位置引数で指定してもよい
# print(sample_text2.split('|', 3))
# print(sample_text2.rsplit('|', 3))
