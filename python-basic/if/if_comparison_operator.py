"""if文基礎
比較演算子を用いたif文の条件判定

[説明ページ]
https://tech.nkhn37.net/python-if-basic/#if-2
"""
# 比較演算子を使った条件分岐
data1 = 'japan'
print(f"data1: {data1}, data1 == 'japan'の評価結果: {data1 == 'japan'}")
if data1 == 'japan':
    print('Japanese')
else:
    print('Unknown')

data2 = 'USA'
print(f"data2: {data2}, data2 == 'japan'の評価結果: {data2 == 'japan'}")
if data2 == 'japan':
    print('Japanese')
else:
    print('Unknown')
