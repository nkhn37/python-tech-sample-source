"""リスト基礎
keyを指定してソートする場合
(sortメソッドでlambdaを使用)

クラスのオブジェクトのリストデータ（属性を使用してソート）

[説明ページ]
https://tech.nkhn37.net/python-list-sort/#i-3
"""


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

# ===== keyを指定してソートする (sortメソッド)
# id属性でソートする場合
data.sort(key=lambda d: d.id)
print(f"data: {data}")
# name属性でソートする場合
data.sort(key=lambda d: d.name)
print(f"data: {data}")
# value属性でソートする場合
data.sort(key=lambda d: d.value)
print(f"data: {data}")
