"""文字列基礎
文字列中の部分文字列の登場回数をカウントする方法
(重複を含めてカウントする方法)

[説明ページ]
https://tech.nkhn37.net/python-substring-count/#i-5
"""
import re

text = "PythonPythonPythonプロジェクトPythonプロジェクトPython"

# 重複を含めてカウントする方法 先読みアサーション(?=...)を使用
ptrn = re.compile(r"(?=(PythonPython))")
result = ptrn.findall(text)
print(len(result))
