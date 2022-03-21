"""文字列基礎
文字列の前から任意の文字を削除する方法 lstrip

[説明ページ]
https://tech.nkhn37.net/python-strip-removeprefix-suffix/#i-4
"""
sample_text = '(---===![Pythonプロジェクト]!===---)'

print(f'"{sample_text.lstrip("(-=![])")}"')
