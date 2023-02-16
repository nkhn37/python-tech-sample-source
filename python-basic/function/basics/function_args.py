"""関数基礎
*argsによる位置引数のタプル受取

[説明ページ]
https://tech.nkhn37.net/python-function-basic/#args
"""


# *argsによる位置引数の受け取り
def print_input(*args):
    print(type(args))
    for i, arg in enumerate(args):
        print(f"arg[{i}] = {arg}")


if __name__ == "__main__":
    print_input(1, 2, "A", "B", [1, 2])
