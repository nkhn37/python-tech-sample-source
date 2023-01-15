"""リスト基礎
keyを指定してソートする場合
(operatorモジュール関数のattrgetterを使用)

クラスのオブジェクトのリストデータ（属性を使用してソート）

[説明ページ]
https://tech.nkhn37.net/python-list-sort/#_attrgetter-2
"""
from operator import attrgetter


class Sample:
    """サンプルクラス"""

    def __init__(self, id, name, value) -> None:
        self.id = id
        self.name = name
        self.value = value

    def __repr__(self) -> str:
        return repr((self.id, self.name, self.value))


data = [
    Sample("ID002", "john", 70),
    Sample("ID001", "mike", 20),
    Sample("ID005", "jane", 1),
    Sample("ID004", "aiko", 50),
    Sample("ID003", "taro", 5),
]

# ===== keyを指定してソートする (sorted関数)
# id属性でソートする場合
sorted_data = sorted(data, key=attrgetter("id"))
print(f"sorted_data: {sorted_data}")
# name属性でソートする場合
sorted_data = sorted(data, key=attrgetter("name"))
print(f"sorted_data: {sorted_data}")
# value属性でソートする場合
sorted_data = sorted(data, key=attrgetter("value"))
print(f"sorted_data: {sorted_data}")
