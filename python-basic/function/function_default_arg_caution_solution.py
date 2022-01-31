"""関数基礎
関数のデフォルト引数に関する注意事項

デフォルト引数にミュータブル（mutable）な型を使うべきではない

問題が発生しうるケースはfunction_default_arg_caution.pyを参照

[解決策]
デフォルト引数にNoneを指定して、Noneの場合に初期化する関数にする

[説明ページ]
https://tech.nkhn37.net/python-function-basic/#i-8
"""


def sample_function(in1, tmp_list=None):
    if tmp_list is None:
        tmp_list = []
    tmp_list.append(in1)
    return tmp_list


if __name__ == '__main__':
    result1 = sample_function('A')
    print(result1)

    result2 = sample_function('B')
    print(result2)
