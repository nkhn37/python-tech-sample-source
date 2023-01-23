"""辞書基礎
辞書を複数のキーと値で更新する方法 (updateメソッド)

[説明ページ]
https://tech.nkhn37.net/python-dict-add-update/#_update
"""
print("===== 辞書を引数に指定する場合")
d = {"k1": 1, "k2": 2}
print(f"d: {d}")

# 辞書を引数に指定する場合
d_add = {"k2": 10, "k3": 20, "k4": 30}
d.update(d_add)
print(f"d: {d}")

# =============================================================================
print("\n===== キーワード引数で指定する場合")
d = {"k1": 1, "k2": 2}
print(f"d: {d}")

# キーワード引数で指定する場合
d.update(k2=10, k3=20, k4=30)
print(f"d: {d}")

# =============================================================================
print("\n===== タプルのリストで指定する場合")
d = {"k1": 1, "k2": 2}
print(f"d: {d}")

# タプルのリストを引数に指定する場合
t_add = [("k2", 10), ("k3", 20), ("k4", 30)]
d.update(t_add)
print(f"d: {d}")
