"""関数基礎
関数のデフォルト値に関する注意事項

デフォルト値にミュータブル（mutable）な型を使うべきではない

[本プログラムは問題が発生しうる例]
この例ではリストの指定がない場合は新しいリストを作ってくれることを想定して作っている
→関数のデフォルト値は最初に１回だけ評価される。
　→リストにどんどん値が追加されてしまい目的に合わない
　　→解決方法については、function_default_arg_caution_solution.pyを参照

[説明ページ]
https://tech.nkhn37.net/python-function-basic/#i-11
"""


# デフォルト値にミュータブル（mutable）な型を使うべきではない
def sample_function(in1, tmp_list=[]):
    tmp_list.append(in1)
    return tmp_list


if __name__ == "__main__":
    result1 = sample_function("A")
    print(result1)

    result2 = sample_function("B")
    print(result2)
