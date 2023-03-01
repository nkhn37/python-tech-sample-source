"""CSVファイルの入出力
ファイルに追記する場合

[説明ページ]
https://tech.nkhn37.net/python-csv/#CSV-2
"""
import csv

data = [1, "XXXXX", "YYYY/MM/DD"]

with open("out_writerow_add.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # writerowやwriterowsで追記
    writer.writerow(data)
