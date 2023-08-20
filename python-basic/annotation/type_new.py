"""型ヒント（変数・関数の型アノテーション）の基本
新しいカスタム型の作成

[説明ページ]
https://tech.nkhn37.net/python-type-annotation-basic/#i-6
"""
from typing import NewType

# 新しいUserId型を作る
UserId = NewType("UserId", int)

# UserId型の変数を用意
test_id = UserId(12345)
print(test_id)
