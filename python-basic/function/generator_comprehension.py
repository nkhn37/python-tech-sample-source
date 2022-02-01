"""ジェネレータ基礎
ジェネレータ内包表記の使い方

[説明ページ]
https://tech.nkhn37.net/python-generator-comprehension/#i

[内包表記まとめページ]
https://tech.nkhn37.net/python-comprehension/
"""
gen = (i for i in range(10) if i % 2 == 0)

print(type(gen))
for i in gen:
    print(i)
