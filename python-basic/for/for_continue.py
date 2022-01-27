"""for文基礎
continue文による次のループへのジャンプ

[説明ページ]
https://tech.nkhn37.net/python-for/#continue
"""
# continue文で次のループへ
data = [10, 20, 30, 40, 50]

for dt in data:
    print(f'start: {dt}')
    if dt < 30:
        # 30より小さい値の場合は、次のループへ
        continue
    print('end')
