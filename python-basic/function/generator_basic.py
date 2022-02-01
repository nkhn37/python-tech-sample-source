"""関数基礎
ジェネレータ(generator)の基本

[説明ページ]
https://tech.nkhn37.net/python-generator-yield/#_yield
"""


# generator sample
def generate_char():
    yield 'A'
    yield 'B'
    yield 'C'


if __name__ == '__main__':
    gen = generate_char()
    print(type(gen))

    # Aが出力される
    print(next(gen))
    # Bが出力される
    print(next(gen))
    # Cが出力される
    print(next(gen))
