"""辞書基礎
keysメソッドを使用してキーに対してfor文を実行する方法

[説明ページ]
https://tech.nkhn37.net/python-dict-keys-values-items/#keysfor
"""
d = {'k1': 10, 'k2': 20, 'k3': 30, 'k4': 40, 'k5': 50}

# for文で値を扱う
for key in d.keys():
    print(f'key: {key}')
