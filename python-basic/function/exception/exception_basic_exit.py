"""関数基礎
例外（exception）の基本的な使い方
（例外をキャッチし、処理を終了する例）

[説明ページ]
https://tech.nkhn37.net/python-exception-try-except-raise/#i-3
"""
import sys

data_list = ["A", "B", "C"]
try:
    print(data_list[5])
except IndexError as ex:
    print(ex)
    sys.exit(1)
print("end")
