"""文字列基礎
数値文字関連の判定メソッド
isdecimal, isdigit, isnumericの結果の違い

[説明ページ]
https://tech.nkhn37.net/python-isxxxxx/#isdecimalisdigitisnumeric
"""
print("--- 半角数字('12345')")
print('12345'.isdecimal())
print('12345'.isdigit())
print('12345'.isnumeric())
print("--- 上付き数字、下付き数字('⁰₀')")
print('⁰₀'.isdecimal())
print('⁰₀'.isdigit())
print('⁰₀'.isnumeric())
print("--- 全角数字('１２３４５')")
print('１２３４５'.isdecimal())
print('１２３４５'.isdigit())
print('１２３４５'.isnumeric())
print("--- 漢数字('一弐参肆伍')")
print('一弐参肆伍'.isdecimal())
print('一弐参肆伍'.isdigit())
print('一弐参肆伍'.isnumeric())
print("--- ローマ数字('ⅠⅡⅢⅣⅤ')")
print('ⅠⅡⅢⅣⅤ'.isdecimal())
print('ⅠⅡⅢⅣⅤ'.isdigit())
print('ⅠⅡⅢⅣⅤ'.isnumeric())
