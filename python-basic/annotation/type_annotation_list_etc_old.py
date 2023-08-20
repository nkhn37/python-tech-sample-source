"""型ヒント（変数・関数の型アノテーション）の基本
リスト・タプル・辞書の型アノテーション
(typingモジュールからのインポート)

[説明ページ]
https://tech.nkhn37.net/python-type-annotation-basic/#i-4
"""
from typing import Dict, List, Tuple

value_list: List[int] = [1, 2, 3, 4, 5]
value_tuple: Tuple[int, str] = (1, "abc")
value_dict: Dict[int, str] = {1: "a", 2: "b", 3: "c"}

print(value_list)
print(value_tuple)
print(value_dict)
