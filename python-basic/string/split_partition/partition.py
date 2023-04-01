"""文字列基礎
文字列を特定の区切り文字で2分割する方法
前方から分割する partition

[説明ページ]
https://tech.nkhn37.net/python-split-splitlines-partition/#2_partition
"""
sample_text = "samplesite.com/sample.html"

# partitionで前方から2分割する
print(sample_text.partition("."))
# 区切り文字が見つからない場合
print(sample_text.partition("#"))
