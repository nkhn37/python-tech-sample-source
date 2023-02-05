"""doctestの使い方
- docstring内にテストコードを記載する
- エラーがない場合にはなにも出力されない
- 詳細を常に出力させたい場合は実行時に「-v」をつけるか、doctest.testmodにverbose=Trueを設定

※テストファイル自体をdoctest.pyという名称にしてしまうとAttributeErrorになるので注意

[説明ページ]
https://tech.nkhn37.net/doctest-basics/
"""


class Sample:
    """Sampleクラス"""

    def add_and_double(self, x, y):
        """xとyを足して2倍した値を返却する

        Args:
            x: 入力値1
            y: 入力値2

        Raises:
            ValueError: int以外の場合

        Returns:
            (x + y) * 2 の計算結果

        >>> tmp = Sample()
        >>> tmp.add_and_double(1, 1)
        4
        >>> tmp.add_and_double(2, 2)
        8
        >>> tmp.add_and_double("1", 1)
        Traceback (most recent call last):
        ...
        ValueError
        """
        # intでない場合は、ValueErrorとする
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError

        # 計算処理
        result = x + y
        result *= 2

        return result


if __name__ == "__main__":
    import doctest

    # doctestを実行
    doctest.testmod()
