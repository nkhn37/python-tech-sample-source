"""関数基礎
例外（exception）の基本的な使い方

[注意]except Exceptionで全ての例外をキャッチするのは止めよう

[説明ページ]
https://tech.nkhn37.net/python-exception-try-except-raise/#except_Exception
"""
data_list = ['A', 'B', 'C']

while True:
    input_value = input('input index (q to quit): ')

    if input_value == 'q':
        break

    try:
        index = int(input_value)
        print(data_list[index])
    except Exception as ex:
        print(f'exception: {ex}')
