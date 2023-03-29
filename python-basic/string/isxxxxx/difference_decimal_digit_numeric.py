"""文字列基礎
数値文字関連の判定メソッド
isdecimal, isdigit, isnumericの結果の違い

[説明ページ]
https://tech.nkhn37.net/python-isxxxxx/#isdecimalisdigitisnumeric
"""
print("--- 半角数字('12345')")
print(f'isdecimal: {"12345".isdecimal()}')
print(f'isdigit: {"12345".isdigit()}')
print(f'isnumeric: {"12345".isnumeric()}')

print("--- 上付き数字、下付き数字('⁰₀')")
print(f'isdecimal: {"⁰₀".isdecimal()}')
print(f'isdigit: {"⁰₀".isdigit()}')
print(f'isnumeric: {"⁰₀".isnumeric()}')

print("--- 全角数字('１２３４５')")
print(f'isdecimal: {"１２３４５".isdecimal()}')
print(f'isdigit: {"１２３４５".isdigit()}')
print(f'isnumeric: {"１２３４５".isnumeric()}')

print("--- 漢数字('一弐参肆伍')")
print(f'isdecimal: {"一弐参肆伍".isdecimal()}')
print(f'isdigit: {"一弐参肆伍".isdigit()}')
print(f'isnumeric: {"一弐参肆伍".isnumeric()}')

print("--- ローマ数字('ⅠⅡⅢⅣⅤ')")
print(f'isdecimal: {"ⅠⅡⅢⅣⅤ".isdecimal()}')
print(f'isdigit: {"ⅠⅡⅢⅣⅤ".isdigit()}')
print(f'isnumeric: {"ⅠⅡⅢⅣⅤ".isnumeric()}')
