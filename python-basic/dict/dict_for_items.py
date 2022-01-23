"""辞書基礎
itemsメソッドを使用して辞書の要素に対してfor文を実行する方法
（キーと値をそれぞれ取得して使う方法）

[説明ページ]
https://tech.nkhn37.net/python-dict-keys-values-items/#i
"""
d = {'k1': 10, 'k2': 20, 'k3': 30, 'k4': 40, 'k5': 50}

# for文で要素（キー、値）を扱う
for key, value in d.items():
    print(f'key: {key}, value: {value}')
