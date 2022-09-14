"""argparseモジュール
基本的な使い方

[説明ページ]
https://tech.nkhn37.net/python-argparse-commandline-args/#argparse
"""
from argparse import ArgumentParser


def main():
    # ===== ArgumentParserの準備
    # パーサーの準備
    parser = ArgumentParser(description='スクリプトの説明')
    # 位置引数の設定
    parser.add_argument('arg1', metavar='Num1', type=int, help='Num1の説明')
    parser.add_argument('arg2', metavar='Str1', type=str, help='Str1の説明')
    # オプション引数の設定
    parser.add_argument('-x', action='store_true', dest='x_opt',
                        help='実行オプション')
    parser.add_argument('-f', '--file', action='store', dest='filename',
                        help='ファイル名オプション')
    # コマンドライン引数をパース(解析)する
    args = parser.parse_args()

    # ===== 取得した引数を取得する
    print(f'filename = {args.filename}')
    print(f'arg1 = {args.arg1}, {type(args.arg1)}')
    print(f'arg2 = {args.arg2}, {type(args.arg2)}')
    print(f'x_opt = {args.x_opt}')

    # =====
    # 実行スクリプト内容を記載
    print('===== スクリプト本体の実行 =====')
    print('..........')
    print('===== スクリプトの終了 =====')
    # =====


if __name__ == '__main__':
    main()
