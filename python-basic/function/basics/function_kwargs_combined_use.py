"""関数基礎
**kwargsによるキーワード引数の辞書受取
(通常の位置引数や*argsとの組み合わせ)

[説明ページ]
https://tech.nkhn37.net/python-function-basic/#args-2
"""


# 通常の位置引数や*argsとの組み合わせ
def print_input(in1, in2, *args, **kwargs):
    print(in1)
    print(in2)
    for i, arg in enumerate(args):
        print(f"arg[{i}] = {arg}")

    for k, v in kwargs.items():
        print(f"key: {k}, value:{v}")


if __name__ == "__main__":
    print_input(1, 2, "A", "B", "C", opt1=1, opt2=2, name="python")
