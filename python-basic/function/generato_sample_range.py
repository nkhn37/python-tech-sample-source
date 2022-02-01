"""関数基礎
ジェネレータ(generator)でrangeと同じ動作を作成してみる

[説明ページ]
https://tech.nkhn37.net/python-generator-yield/#range
"""


# sample range function
def sample_range(start=0, stop=10, step=1):
    num = start
    while num < stop:
        yield num
        num += step


if __name__ == '__main__':
    iter_range = sample_range(0, 5)
    print(type(iter_range))
    print(next(iter_range))
    print(next(iter_range))
    print(next(iter_range))

    print('======================')
    for i in iter_range:
        print(i)
