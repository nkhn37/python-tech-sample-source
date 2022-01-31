"""関数基礎
*argsによる位置引数のタプル受取
（通常の位置引数との併用）

[説明ページ]
https://tech.nkhn37.net/python-function-basic/#args
"""


def print_input(input1, input2, *args):
    print(input1)
    print(input2)
    for i, arg in enumerate(args):
        print(f'arg[{i}] = {arg}')


if __name__ == '__main__':
    print_input(1, 2, 'A', 'B', 'C')
