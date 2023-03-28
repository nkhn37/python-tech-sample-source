"""
文字列中の部分文字列の登場回数をカウントする方法
(reを使って、大文字・小文字を区別しないでカウントする)

[説明ページ]
https://tech.nkhn37.net/python-substring-count/#i-4
"""
import re

text = "PythonPythonPythonプロジェクトPythonプロジェクトPython"

# 大文字・小文字を区別しないでカウントする
ptrn = re.compile("python", re.IGNORECASE)
result = ptrn.findall(text)
print(len(result))

ptrn = re.compile("PYTHON", re.IGNORECASE)
result = ptrn.findall(text)
print(len(result))
