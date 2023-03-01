"""CSVファイルの入出力
区切り文字を指定する場合(delimiter引数)

[説明ページ]
https://tech.nkhn37.net/python-csv/#delimiter
"""
import csv

with open("sample_tab.csv", "r", encoding="utf-8") as file:
    # delimiterで区切り文字を指定
    reader = csv.reader(file, delimiter="\t")
    # データを取得する
    data = [row for row in reader]

print(data)
