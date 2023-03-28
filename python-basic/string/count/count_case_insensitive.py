"""文字列基礎
文字列中の部分文字列の登場回数をカウントする方法
(大文字・小文字を区別しないでカウントする)

[説明ページ]
https://tech.nkhn37.net/python-substring-count/#i-3
"""
text = "PythonPythonPythonプロジェクトPythonプロジェクトPython"

# 大文字・小文字を区別しないでカウントする
print(text.lower().count("python"))
print(text.upper().count("PYTHON"))
