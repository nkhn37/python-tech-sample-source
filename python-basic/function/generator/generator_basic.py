"""関数基礎
ジェネレータ(generator)の基本
yieldによる返却

[説明ページ]
https://tech.nkhn37.net/python-generator-yield/#yield
"""


# generator関数
def generate_char():
    yield "A"
    yield "B"
    yield "C"


if __name__ == "__main__":
    gen = generate_char()
    print(type(gen))

    # Aが出力される
    print(next(gen))
    # Bが出力される
    print(next(gen))
    # Cが出力される
    print(next(gen))
