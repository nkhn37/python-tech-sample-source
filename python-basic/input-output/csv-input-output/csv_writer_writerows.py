"""CSVファイルの入出力
write関数のwriterowsで複数行をまとめて書き込む

[説明ページ]
https://tech.nkhn37.net/python-csv/#_writerows
"""
import csv

data = [
    [1, "田中太郎", "2021/1/1"],
    [2, "伊藤洋子", "2020/9/1"],
    [3, "佐藤花子", "2019/1/1"],
]

with open("out_writerows.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # writerowsでまとめて書き込み
    writer.writerows(data)
