"""pytestの使い方
テスト用コード

[説明ページ]
https://tech.nkhn37.net/pytest-basics/
"""
import pytest

import sample


# スキップ用フラグ
SKIP_FLAG = True


class TestSample:
    """Sampleクラスのテスト用クラス"""

    @classmethod
    def setup_class(cls):
        print("\nStart TestSample")
        cls.temp = sample.Sample()

    @classmethod
    def teardown_class(cls):
        print("\nEnd of TestSample")
        del cls.temp

    def setup_method(self, method):
        print(f"\nStart method name: {method.__name__}")

    def teardown_method(self, method):
        print(f"\nEnd method name: {method.__name__}")

    def test_add_and_double(self):
        """テストケース1: 正常計算"""
        assert self.temp.add_and_double(1, 1) == 4
        assert self.temp.add_and_double(2, 2) == 8

    def test_add_and_double_raise(self):
        """テストケース2: 例外処理"""
        with pytest.raises(ValueError):
            self.temp.add_and_double("1", 1)
        with pytest.raises(ValueError):
            self.temp.add_and_double(1, "1")
        with pytest.raises(ValueError):
            self.temp.add_and_double("1", "1")

    @pytest.mark.skip(reason="skip理由:xxxxxxxxxx")
    def test_add_and_double_skip(self):
        """スキップ確認用"""
        assert self.temp.add_and_double(1, 1) == 4

    @pytest.mark.skipif(SKIP_FLAG is True, reason="条件付きskip理由:xxxxxxxxx")
    def test_add_and_double_skipif(self):
        """条件付きスキップ確認用"""
        assert self.temp.add_and_double(1, 1) == 4

    def test_add_and_double_option(self, request):
        """フィクスチャを使ってテストする場合
        ※requestはpytestで定義されているフィクスチャなのでこのように使うものと覚える

        Args:
            request: フィクスチャ
        """
        os_name = request.config.getoption("--os-name")
        if os_name == "windows":
            print("dir")
        elif os_name == "linux" or os_name == "mac":
            print("ls")
        assert self.temp.add_and_double(1, 1) == 4

    def test_add_and_double_original(self, target_numbers):
        """独自フィクスチャを使ってテストする場合

        Args:
            target_numbers: テスト対象数値リストを返す独自フィクスチャ
        """
        print(target_numbers)
        assert self.temp.add_and_double(1, 1) == 4

    def test_add_and_double_original_csv(self, open_csv_file):
        """独自フィクスチャを使ってテストする場合
        csvファイルなどのオープン/クローズをフィクスチャ側で実行

        Args:
            open_csv_file: csvファイルを開く独自フィクスチャ
        """
        print(open_csv_file)
        open_csv_file.write("test1,test2,test3")
        assert self.temp.add_and_double(1, 1) == 4
