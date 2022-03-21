"""文字列基礎
文字列から接尾辞(suffix)を削除する方法 removesuffix

[説明ページ]
https://tech.nkhn37.net/python-strip-removeprefix-suffix/#suffix_removesuffix
"""
sample_text_pre = 'Testプロジェクト'
sample_text_suf = 'プロジェクトTest'

# removesuffixで接尾辞（suffix）を削除する
print('--- removesuffix')
print(sample_text_pre.removesuffix('Test'))
print(sample_text_suf.removesuffix('Test'))
