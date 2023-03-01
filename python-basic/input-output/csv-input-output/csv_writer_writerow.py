"""CSVファイルの入出力
writer関数のwriterowで1行ずつ書き込む

[説明ページ]
https://tech.nkhn37.net/python-csv/#_writerow
"""
import csv

data = [
    [1, "田中太郎", "2021/1/1"],
    [2, "伊藤洋子", "2020/9/1"],
    [3, "佐藤花子", "2019/1/1"],
]

with open("out_writerow.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # writerowで1行ずつ書き込み
    writer.writerow(data[0])
    writer.writerow(data[1])
    writer.writerow(data[2])
