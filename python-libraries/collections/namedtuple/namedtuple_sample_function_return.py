"""Collectionsモジュール
名前付きタプル namedtupleの使いどころ
関数の戻り値で使用する

[説明ページ]
https://tech.nkhn37.net/python-collections-namedtuple/#i
"""
import collections
import statistics


def calculate_stat(data):
    min_v = min(data)
    max_v = max(data)
    mean_v = statistics.mean(data)
    var_v = statistics.variance(data)
    std_v = statistics.stdev(data)

    # 返却値をnamedtupleで定義
    Stat = collections.namedtuple("Stat", ["min", "max", "mean", "var", "std"])
    stats = Stat(min_v, max_v, mean_v, var_v, std_v)
    return stats


def main():
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    result = calculate_stat(values)
    print(
        f"min:{result.min}, "
        f"max:{result.max}, "
        f"mean:{result.mean}, "
        f"var:{result.var}, "
        f"std:{result.std}"
    )


if __name__ == "__main__":
    main()
