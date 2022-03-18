"""文字列基礎
文字列が特定の文字列で終わることを判定する endswithメソッド
notによる反転

[説明ページ]
https://tech.nkhn37.net/python-in-startswith-endswith/#_endswith
"""
sample_text = 'Pythonプロジェクト'

# endswithによる判定 notによる反転
print('--- endswith')
print(not sample_text.endswith('Python'))
print(not sample_text.endswith('プロジェクト'))
