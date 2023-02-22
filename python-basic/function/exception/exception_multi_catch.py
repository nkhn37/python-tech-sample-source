"""関数基礎
例外（exception）の基本的な使い方
（複数の例外のキャッチ）

[説明ページ]
https://tech.nkhn37.net/python-exception-try-except-raise/#i-4
"""
data_list = ["A", "B", "C"]

while True:
    input_value = input("input index (q to quit): ")

    if input_value == "q":
        break

    try:
        index = int(input_value)
        print(data_list[index])
    except IndexError as ex:
        print(f"bad index : {ex}")
    except ValueError as ex:
        print(f"bad value : {ex}")
