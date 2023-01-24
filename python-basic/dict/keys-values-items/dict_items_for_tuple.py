"""辞書基礎
itemsメソッドを使用して辞書の要素に対してfor文を実行する方法
（tupleで要素を受け取って使用する方法）

[説明ページ]
https://tech.nkhn37.net/python-dict-keys-values-items/#tuple
"""
d = {"k1": 10, "k2": 20, "k3": 30, "k4": 40, "k5": 50}

# for文で要素（キー、値）をタプルとして受け取って扱う
for tpl in d.items():
    print(f"key: {tpl[0]}, value: {tpl[1]}")
