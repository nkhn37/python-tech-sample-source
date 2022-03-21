"""文字列基礎
文字列の後から空白等の文字列を削除する方法 rstrip

[説明ページ]
https://tech.nkhn37.net/python-strip-removeprefix-suffix/#i-5
"""
sample_text = ' 　Pythonプロジェクト　 \t\n'

print(f'"{sample_text.rstrip()}"')
