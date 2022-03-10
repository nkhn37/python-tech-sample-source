"""文字列基礎
lowerより強力に大文字→小文字変換する casefoldメソッド

[説明ページ]
https://tech.nkhn37.net/python-upper-lower-translation/#lower_casefold
"""
data = 'Fußball'
print(f'元の文字列: {data}')
print(f'casefold: {data.casefold()}')
print(f'lower: {data.lower()}')
