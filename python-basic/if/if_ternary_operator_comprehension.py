"""if文基礎
リスト内包表記と三項演算子の組み合わせ

[説明ページ]
https://tech.nkhn37.net/python-if-basic/#i-4
"""
# リスト内包表記と三項演算子の組み合わせ
result = ["even" if i % 2 == 0 else "odd" for i in range(10)]
print(result)
