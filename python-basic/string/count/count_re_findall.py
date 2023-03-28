"""文字列基礎
正規表現に一致する部分文字列の登場回数をカウントする方法
(正規表現モジュール reを使用する場合)

[説明ページ]
https://tech.nkhn37.net/python-substring-count/#findall
"""
import re

text = "PythonPythonPythonプロジェクトPythonプロジェクトPython"

# reを使って部分文字列をカウントする
ptrn = re.compile("Python")
result = ptrn.findall(text)
print(len(result))

# 重複のない出現回数をカウントするので注意
ptrn = re.compile("PythonPython")
result = ptrn.findall(text)
print(len(result))
