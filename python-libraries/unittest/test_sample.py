"""unittestの使い方
テスト用コード

[説明ページ]
https://tech.nkhn37.net/unittest-basics/
"""
import unittest

import sample

# スキップ用フラグ
SKIP_FLAG = True


class TestSample(unittest.TestCase):
    """Sampleクラスのテスト用クラス"""

    @classmethod
    def setUpClass(cls):
        print("\nStart TestSample")
        cls.temp = sample.Sample()

    @classmethod
    def tearDownClass(cls):
        print("\nEnd of TestSample")
        del cls.temp

    def setUp(self):
        print("\nTest Start")

    def tearDown(self):
        print("End of Test")

    def test_add_and_double(self):
        """テストケース1: 正常計算"""
        self.assertEqual(self.temp.add_and_double(1, 1), 4)
        self.assertEqual(self.temp.add_and_double(2, 2), 8)
        # self.assertEqual(self.temp.add_and_double(2, 2), 4)

    def test_add_and_double_raise(self):
        """テストケース2: 例外処理"""
        with self.assertRaises(ValueError):
            self.temp.add_and_double("1", 1)
        with self.assertRaises(ValueError):
            self.temp.add_and_double(1, "1")
        with self.assertRaises(ValueError):
            self.temp.add_and_double("1", "1")
        # with self.assertRaises(ValueError):
        #     self.temp.add_and_double(1, 1)

    @unittest.skip("skip理由:xxxxxxxxxx")
    def test_add_and_double_skip(self):
        """スキップ確認用"""
        assert self.temp.add_and_double(1, 1) == 4

    @unittest.skipIf(SKIP_FLAG is True, "条件付きskip理由:xxxxxxxxx")
    def test_add_and_double_skipif(self):
        """条件付きスキップ確認用"""
        assert self.temp.add_and_double(1, 1) == 4


if __name__ == "__main__":
    # unittestを実行する
    unittest.main()
