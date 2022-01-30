"""while文基礎
elseによる正常終了の確認

[説明ページ]
https://tech.nkhn37.net/python-while-basic/#else
"""
# 正常終了する場合
data = ['A', 'B', 'C']
idx = 0
while idx < len(data):
    if data[idx] == 'Z':
        break
    print(f'data[{idx}] = {data[idx]}')
    idx += 1
else:
    print('処理正常終了')

print('=====')
# 正常終了しない場合
data = ['A', 'B', 'Z', 'C']
idx = 0
while idx < len(data):
    if data[idx] == 'Z':
        break
    print(f'data[{idx}] = {data[idx]}')
    idx += 1
else:
    print('処理正常終了')
