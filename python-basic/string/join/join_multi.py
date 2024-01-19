"""文字列基礎
リストを連結・結合して文字列にする join
異なる型が混在している場合

[説明ページ]
https://tech.nkhn37.net/python-str-join/#i-8
"""


class CustomClass1:
    pass


class CustomClass2:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"<CustomClass2 value={self.value}>"


# 様々な型が混在している場合
sample_list = [1, 2, "a", "b", CustomClass1(), CustomClass2(123), 8.0, 9.0]

# strで文字列に変換ができれば結合可能
print(",".join([str(i) for i in sample_list]))
