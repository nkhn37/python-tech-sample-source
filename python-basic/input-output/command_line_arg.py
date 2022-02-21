"""入出力基礎
コマンドライン引数の取得方法（sys）

[説明ページ]
https://tech.nkhn37.net/python-sys-commandline-args/
"""
import sys


def main():
    # コマンドライン引数を取得する
    args = sys.argv
    # コマンドライン引数を表示する
    print(f'args: {args}, {type(args)}')

    # コマンドライン引数の数を調べる
    print(f'len(args): {len(args)}')

    # コマンドライン引数を順番に処理する
    for i, arg in enumerate(args):
        print(f'arg[{i}] = {arg}')


if __name__ == '__main__':
    main()
