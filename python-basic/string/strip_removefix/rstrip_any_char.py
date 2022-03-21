"""文字列基礎
文字列の後から任意の文字列を削除する方法 rstrip

[説明ページ]
https://tech.nkhn37.net/python-strip-removeprefix-suffix/#i-6
"""
sample_text = '(---===![Pythonプロジェクト]!===---)'

print(f'"{sample_text.rstrip("(-=![])")}"')
