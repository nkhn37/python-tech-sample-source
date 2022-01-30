"""if文基礎
if文におけるTrue, Falseの考え方
Pythonではnull値や0、空のリスト等はFalseとして扱う
本プログラムは空のリストの場合の判定例を示したもの

[説明ページ]
https://tech.nkhn37.net/python-if-basic/#TrueFalse
"""
# 空リストの判定
data_l = []
if data_l:
    print('リストには値が入っています。')
else:
    print('リストは空です。')

data_l = [10, 20, 30]
if data_l:
    print('リストには値が入っています。')
else:
    print('リストは空です。')
