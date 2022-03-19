"""文字列基礎
文字列を改行文字で分割する方法 splitlines

[説明ページ]
https://tech.nkhn37.net/python-split-splitlines-partition/#_splitlines
"""
sample_text = '''\
Python
Java
C
C++
C#
Go
'''

# splitlinesにより改行文字で分割する
print(sample_text.splitlines())
# 改行文字を含めたまま分割する場合は、引数にTrueを設定する
print(sample_text.splitlines(True))
