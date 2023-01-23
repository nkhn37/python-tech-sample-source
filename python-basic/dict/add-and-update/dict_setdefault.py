"""辞書基礎
辞書にキーが存在しない時のみ要素を追加する方法 (setdefaultメソッド)

[説明ページ]
https://tech.nkhn37.net/python-dict-add-update/#_setdefault
"""
# 辞書を定義する
d = {"k1": 1, "k2": 2}
print(f"d: {d}\n")

# setdefaultを使って要素を追加
# キーが存在しない場合
print(d.setdefault("k3", 3))
print(f"d: {d}")

# キーが存在する場合
print(d.setdefault("k1", 5))
print(f"d: {d}")
