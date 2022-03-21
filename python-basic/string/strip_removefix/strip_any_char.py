"""文字列基礎
文字列の前後から任意の文字を削除する方法 strip

[説明ページ]
https://tech.nkhn37.net/python-strip-removeprefix-suffix/#i-2
"""
sample_text = '(---===![Pythonプロジェクト]!===---)'

print(f'"{sample_text.strip("(-=![])")}"')
