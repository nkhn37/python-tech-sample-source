"""ジェネレータ基礎
ジェネレータ内包表記の使い方
（タプルで取り込んで使う方法）

[説明ページ]
https://tech.nkhn37.net/python-generator-comprehension/#i

[内包表記まとめページ]
https://tech.nkhn37.net/python-comprehension/
"""
tpl = tuple(i for i in range(10) if i % 2 == 0)

print(type(tpl))
print(tpl)
