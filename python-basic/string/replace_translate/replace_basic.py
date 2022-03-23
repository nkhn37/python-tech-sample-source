"""文字列基礎
特定の部分文字列を別の文字列に置き換える replaceメソッド

[説明ページ]
https://tech.nkhn37.net/python-replace-translate/#_replace
"""
sample_text = 'Pythonプロジェクトを作成してPythonを学習しよう！'

print(sample_text.replace('Python', 'Java'))
print(sample_text.replace('Python', 'Java', 1))
