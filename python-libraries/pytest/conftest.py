"""pytestの使い方
pytestに関する各種設定を定義する

[説明ページ]
https://tech.nkhn37.net/pytest-basics/
"""
import pytest


def pytest_addoption(parser):
    """テストオプション用の関数"""
    parser.addoption("--os-name", default="windows", help="os name")


@pytest.fixture()
def target_numbers():
    """テスト対象数値リストを返却する

    Returns:
        テスト対象数値リスト
    """
    return [1, 5, 10]


@pytest.fixture()
def open_csv_file():
    """csvファイルをオープンして渡す
    yieldを使用することで終了時にファイルクローズする

    Yields:
        csvファイルオブジェクト
    """
    print("before open")
    with open("test.csv", "w+", encoding="utf-8") as csv_file:
        yield csv_file
    print("\nafter")
