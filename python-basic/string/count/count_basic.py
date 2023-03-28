"""文字列基礎
文字列中の部分文字列の登場回数をカウントする方法

[説明ページ]
https://tech.nkhn37.net/python-substring-count/#i-2
"""
text = "PythonPythonPythonプロジェクトPythonプロジェクトPython"

# countで部分文字列をカウントする
print(text.count("Python"))

# countは重複のない出現回数をカウントするので注意
print(text.count("PythonPython"))
