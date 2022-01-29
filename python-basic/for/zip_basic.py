"""for文基礎
zip関数で複数リストをまとめてfor文で処理する方法
（基本的な使い方）

[説明ページ]
https://tech.nkhn37.net/python-for-zip/#zipfor
"""
# zip関数
data1 = [10, 20, 30, 40, 50]
data2 = ['A', 'B', 'C', 'D', 'E']

for dt1, dt2 in zip(data1, data2):
    print(f'dt1: {dt1}, dt2: {dt2}')
