"""文字列基礎
文字列が特定の文字列で始まることを判定する startswithメソッド

[説明ページ]
https://tech.nkhn37.net/python-in-startswith-endswith/#_startswith
"""
sample_text = "Pythonプロジェクト"

# startswithによる判定
print("--- startswith")
print(sample_text.startswith("Python"))
print(sample_text.startswith("プロジェクト"))
