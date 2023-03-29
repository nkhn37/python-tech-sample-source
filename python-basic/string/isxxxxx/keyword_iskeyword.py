"""文字列基礎
予約済み識別子か判定する
keywordモジュールのiskeyword

[説明ページ]
https://tech.nkhn37.net/python-isxxxxx/#_keywordiskeyword
"""
from keyword import iskeyword

print("python")
print(f"identifier: {'python'.isidentifier()}")
print(f"iskeyword: {iskeyword('python')}\n")

# 予約済みキーワードの場合
print("class")
print(f"identifier: {'class'.isidentifier()}")
print(f"iskeyword: {iskeyword('class')}")
