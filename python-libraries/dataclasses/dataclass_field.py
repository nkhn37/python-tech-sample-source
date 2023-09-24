"""dataclassの使い方の基本
デフォルト値の割り当て field

[説明ページ]
https://tech.nkhn37.net/python-dataclass-basics/#i-3
"""
from dataclasses import dataclass, field


@dataclass
class DataWithDefaults:
    """デフォルト値の設定"""

    immutable: str = field(default="")
    mutable: list = field(default_factory=list)

    def set_data(self, value):
        self.immutable = value
        self.mutable.append(value)


if __name__ == "__main__":
    test1 = DataWithDefaults()
    test2 = DataWithDefaults()

    test1.set_data("data1-1")
    test1.set_data("data1-2")
    test2.set_data("data2-1")

    # インスタンスの属性を確認
    print(test1.immutable)
    print(test1.mutable)
    print(test2.immutable)
    print(test2.mutable)
