"""文字列基礎
リストを結合して文字列にする方法 join
基本的な使い方

[説明ページ]
https://tech.nkhn37.net/python-str-join/#i
"""
sample_list = ['Pytho', 'Java', 'Go', 'C', 'C#']

# 文字列をそのまま結合
print(''.join(sample_list))

# 区切り文字でjoinで結合
print(','.join(sample_list))
