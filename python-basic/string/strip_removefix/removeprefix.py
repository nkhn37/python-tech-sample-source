"""文字列基礎
文字列から接頭辞(prefix)を削除する方法 removeprefix

[説明ページ]
https://tech.nkhn37.net/python-strip-removeprefix-suffix/#prefix_removeprefix
"""
sample_text_pre = 'Testプロジェクト'
sample_text_suf = 'プロジェクトTest'

# removeprefixで接頭辞（prefix）を削除する
print('--- removeprefix')
print(sample_text_pre.removeprefix('Test'))
print(sample_text_suf.removeprefix('Test'))
