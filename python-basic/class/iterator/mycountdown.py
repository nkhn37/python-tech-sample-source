"""イテレータ（iteratorの基本）
独自のカスタムイテレータの作成

[説明ページ]
https://tech.nkhn37.net/python-iterator-basics/#iterator-3
"""


class MyCountDown:
    """カウントダウンイテレータ"""

    def __init__(self, count):
        self.count = count

    def __next__(self):
        """次の値を返す"""
        # 繰り返しの終わりではStopIteration例外を送出する
        if self.count <= 0:
            raise StopIteration
        # カウントダウン
        self.count -= 1
        # 次の値を返す
        return self.count

    def __iter__(self):
        """イテレータの状態を返す"""
        # イテレータ自身を返却
        return self


def main():
    count_iter = MyCountDown(5)
    for c in count_iter:
        print(c)


if __name__ == "__main__":
    main()
