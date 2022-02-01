"""ジェネレータ基礎
ジェネレータ内包表記を使用しない場合の記載
（ジェネレータ内包表記版はgenerator_comprehension.pyを参照）

ジェネレータ内包表記は表記がシンプルになるだけでなく、速度も高速なことから
同じ書き方ができる場合は、ジェネレータ内包表記を利用することを検討しましょう。

[説明ページ]
https://tech.nkhn37.net/python-generator-comprehension/#i

[内包表記まとめページ]
https://tech.nkhn37.net/python-comprehension/
"""


def generate_num():
    for g in range(10):
        if g % 2 == 0:
            yield g


gen = generate_num()
print(type(gen))
for i in gen:
    print(i)
