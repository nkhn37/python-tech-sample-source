"""for文基礎
break文によるループの終了

[説明ページ]
https://tech.nkhn37.net/python-for/#break
"""
# break文でループを抜ける
data = [10, 20, 30, 40, 50]

for dt in data:
    print(f'start: {dt}')
    if dt > 30:
        # 30より大きい値の場合はループを抜ける
        print('break')
        break
    print('end')
