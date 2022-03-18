"""文字列基礎
文字列が特定の文字列で終わることを判定する endswithメソッド

[説明ページ]
https://tech.nkhn37.net/python-in-startswith-endswith/#_endswith
"""
sample_text = 'Pythonプロジェクト'

# endswithによる判定
print('--- endswith')
print(sample_text.endswith('Python'))
print(sample_text.endswith('プロジェクト'))
