"""CSVファイルの入出力
DictReaderを使ってヘッダーがないCSVファイルを列名指定をして読み込む (fieldnames引数)

[説明ページ]
https://tech.nkhn37.net/python-csv/#CSV_fieldnames
"""
import csv

with open("sample.csv", "r", encoding="utf-8") as file:
    dict_reader = csv.DictReader(file, fieldnames=["id", "name", "date"])
    # データを取得する
    data = [row for row in dict_reader]

# データを表示
print(data, "\n")

# 1行目のデータを表示
print(data[0]["id"])
print(data[0]["name"])
print(data[0]["date"])
