"""辞書基礎
辞書にキーと値を追加・更新する方法

[説明ページ]
https://tech.nkhn37.net/python-dict-add-update/#i-2
"""
# 辞書を定義する
d = {"k1": 1, "k2": 2}
print(f"d: {d}")

# 辞書データを参照する
print(f"d['k1']: {d['k1']}")
print(f"d['k2']: {d['k2']}")

# 辞書に要素を追加する
print("\n=== 要素を追加")
d["k3"] = 3
print(f"d: {d}")

# 辞書の要素を更新する
print("\n=== 要素を更新")
d["k1"] = 5
print(f"d: {d}")
