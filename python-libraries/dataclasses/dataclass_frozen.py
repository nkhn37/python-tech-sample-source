"""dataclassの使い方の基本
イミュータブル(immutable)なデータクラスを定義する場合: frozen

[説明ページ]
https://tech.nkhn37.net/python-dataclass-basics/#immutable_frozen
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class FrozenPoint:
    """位置クラス"""

    x: int
    y: int

    def __add__(self, other):
        """+演算子"""
        return FrozenPoint(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """-演算子"""
        return FrozenPoint(self.x - other.x, self.y - other.y)


if __name__ == "__main__":
    point1 = FrozenPoint(1, 1)

    point1.x = 2
    print(point1)
