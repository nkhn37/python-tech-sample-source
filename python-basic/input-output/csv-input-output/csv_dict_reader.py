"""CSVファイルの入出力
DictReaderを使った辞書形式での読み込み

[説明ページ]
https://tech.nkhn37.net/python-csv/#i-2
"""
import csv

with open("sample_header.csv", "r", encoding="utf-8") as file:
    dict_reader = csv.DictReader(file)
    # データを取得する
    data = [row for row in dict_reader]

# データを表示
print(data, "\n")

# 1行目のデータを表示
print(data[0]["id"])
print(data[0]["name"])
print(data[0]["date"])
