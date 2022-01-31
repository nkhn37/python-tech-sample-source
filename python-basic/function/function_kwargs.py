"""関数基礎
**kwargsによるキーワード引数の辞書受取

[説明ページ]
https://tech.nkhn37.net/python-function-basic/#kwargs
"""


def print_input(**kwargs):
    print(type(kwargs))
    for k, v in kwargs.items():
        print(f'key: {k}, value:{v}')


if __name__ == '__main__':
    print_input(opt1=1, opt2=2, value='python')
