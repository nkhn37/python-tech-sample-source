"""for文基礎
elseによる正常終了の確認

[説明ページ]
https://tech.nkhn37.net/python-for/#else
"""
# elseによるbreakのチェック（breakが呼び出されるケース）
data = [10, 20, 30, 40, 50]

for dt in data:
    print(f'start: {dt}')
    if dt > 30:
        # 30より大きい値の場合はループを抜ける
        break
    print('end')
else:
    # breakが呼び出されなければ実行
    print('正常終了')

print('===')
# elseによるbreakのチェック（breakが呼び出されないケース）
data = [10, 20, 30]

for dt in data:
    print(f'start: {dt}')
    if dt > 30:
        # 30より大きい値の場合はループを抜ける
        break
    print('end')
else:
    # breakが呼び出されなければ実行
    print('正常終了')
