"""関数基礎
ジェネレータ(generator)のfor文での使用例

[説明ページ]
https://tech.nkhn37.net/python-generator-yield/#_yield
"""


# generator sample
def generate_char():
    yield 'A'
    yield 'B'
    yield 'C'


if __name__ == '__main__':
    for s in generate_char():
        print(s)
