"""Collectionsモジュール
Counterの使用例：ファイル中の単語数をカウントする

[説明ページ]
https://tech.nkhn37.net/python-collections-counter/#i
"""
import collections
import re

with open('input.txt', 'r', encoding='UTF-8') as f:
    words = re.findall(r'\w+', f.read().lower())

print(f'words = {words}')

print('=====')
counter = collections.Counter(words)
print(counter)
print(counter.most_common(3))
