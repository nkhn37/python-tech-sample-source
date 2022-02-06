"""関数基礎
lambda関数（無名関数）の使い方

[説明ページ]
https://tech.nkhn37.net/python-lambda/#lambda-2
"""
# lambda function
func = lambda val1, val2: val1 * 2 + val2 * 2

print(type(func))
print(func(1, 2))
print(func(3, 4))
