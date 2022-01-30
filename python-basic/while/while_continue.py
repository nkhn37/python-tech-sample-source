"""while文基礎
continue文による次のループへのジャンプ

[説明ページ]
https://tech.nkhn37.net/python-while-basic/#continue
"""
# continue文で次のループへ
while True:
    value = input("偶数を入力してください（終了する場合は'q'）: ")
    if value == 'q':
        break
    elif int(value) % 2 != 0:
        # 奇数の場合は次のループへ
        continue
    print(f'偶数の入力値は、{value}です。')
