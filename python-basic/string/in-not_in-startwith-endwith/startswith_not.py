"""文字列基礎
文字列が特定の文字列で始まることを判定する startswithメソッド
notによる反転

[説明ページ]
https://tech.nkhn37.net/python-in-startswith-endswith/#_startswith
"""
sample_text = "Pythonプロジェクト"

# startswithによる判定 notによる反転
print("--- not startswith")
print(not sample_text.startswith("Python"))
print(not sample_text.startswith("プロジェクト"))
