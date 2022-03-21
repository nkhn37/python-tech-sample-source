"""文字列基礎
文字列の前から空白等の文字を削除する方法 lstrip

[説明ページ]
https://tech.nkhn37.net/python-strip-removeprefix-suffix/#i-3
"""
sample_text = ' 　Pythonプロジェクト　 \t\n'

print(f'"{sample_text.lstrip()}"')
