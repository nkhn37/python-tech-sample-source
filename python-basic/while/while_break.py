"""while文基礎
break文によるループの終了

[説明ページ]
https://tech.nkhn37.net/python-while-basic/#break
"""
# breakでループを抜ける
while True:
    value = input("値を入力してください（終了する場合は'q'）: ")
    if value == 'q':
        break
    print(f'入力値は、{value}です。')
