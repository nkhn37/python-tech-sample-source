"""辞書基礎
辞書を結合・更新する方法 (|演算子、|=演算子)

【注意点】辞書に対する |演算子、|=演算子は、Python3.9より使用可能になっているため、
それ以前のバージョンで実行すると「TypeError」 となるので注意してください。

[説明ページ]
https://tech.nkhn37.net/python-dict-add-update/#_Python39

[Python3.9ドキュメント]
https://docs.python.org/ja/3.9/whatsnew/3.9.html#dictionary-merge-update-operators
"""
print("===== |演算子を使用した辞書の結合")
d1 = {"k1": 1, "k2": 2}
print(f"d1: {d1}")
d2 = {"k2": 10, "k3": 20, "k4": 30}
print(f"d2: {d2}")

# |演算子を使用
print(f"d1|d2 : {d1|d2}")
print(f"d2|d1 : {d2|d1}")

# =============================================================================
print("\n===== |=演算子を使用した辞書の結合")
d1 = {"k1": 1, "k2": 2}
print(f"d1: {d1}")
d2 = {"k2": 10, "k3": 20, "k4": 30}
print(f"d2: {d2}")

# |=演算子を使用
d1 |= d2
print(f"d1: {d1}")
