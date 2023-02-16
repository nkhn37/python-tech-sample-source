"""関数基礎
関数の引数と返り値の宣言方法

[説明ページ]
https://tech.nkhn37.net/python-function-basic/#i-3
"""


# 関数定義 引数、返却値
def func_2(num):
    return 2 * num


if __name__ == "__main__":
    x1 = 5
    y1 = func_2(x1)
    print(f"x1 = {x1}, y1 = {y1}")

    x2 = 10
    y2 = func_2(x2)
    print(f"x2 = {x2}, y2 = {y2}")
