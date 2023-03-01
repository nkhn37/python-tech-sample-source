"""CSVファイルの入出力
reader関数を使用した基本的な読み込み方法

[説明ページ]
https://tech.nkhn37.net/python-csv/#i
"""
import csv

with open("sample.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    # データを取得する
    data = [row for row in reader]

print(data)
