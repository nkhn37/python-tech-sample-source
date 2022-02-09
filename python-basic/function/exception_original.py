"""関数基礎
例外（exception）の基本的な使い方
（独自例外の作成方法と例外のスロー）

[説明ページ]
https://tech.nkhn37.net/python-exception-try-except-raise/#raise
"""


class MyException(Exception):
    pass


def my_original_method(value):
    if value < 0:
        raise MyException('minus value is not allowed')
    else:
        return value


def main():
    value = -10
    try:
        print(my_original_method(value))
    except MyException as ex:
        print(ex)


if __name__ == '__main__':
    main()
