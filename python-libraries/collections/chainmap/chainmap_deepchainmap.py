"""Collectionsモジュール
ChainMapでチェーン上の辞書を更新、削除する
（DeepChainMapクラスの作成による対応）

[説明ページ]
https://tech.nkhn37.net/python-collections-chainmap/#ChainMap-4
"""
import collections


class DeepChainMap(collections.ChainMap):
    def __setitem__(self, key, value):
        for mapping in self.maps:
            if key in mapping:
                mapping[key] = value
                return
        self.maps[0][key] = value

    def __delitem__(self, key):
        for mapping in self.maps:
            if key in mapping:
                del mapping[key]
                return
        raise KeyError(key)


def main():
    dict_a = {"a": "A"}
    dict_b = {"b": "B"}
    dict_c = {"c": "C"}

    deep_m = DeepChainMap(dict_c, dict_b, dict_a)
    print(deep_m)

    print("=====")
    # キーが"b"であるものを探索して更新する
    deep_m["b"] = "b_update"
    print(deep_m)

    print("=====")
    # キーが"a"であるものを探索して削除する
    del deep_m["a"]
    print(deep_m)


if __name__ == "__main__":
    main()
