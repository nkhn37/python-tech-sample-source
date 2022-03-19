"""文字列基礎
文字列を特定の区切り文字で2分割する方法
後方から分割する rpartition

[説明ページ]
https://tech.nkhn37.net/python-split-splitlines-partition/#2_rpartition
"""
sample_text = 'samplesite.com/sample.html'

# rpartitionで後方から2分割する
print(sample_text.rpartition('.'))
# 区切り文字が見つからない場合
print(sample_text.rpartition('#'))
