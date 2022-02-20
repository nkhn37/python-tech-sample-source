"""入出力基礎
CSVファイルの入出力（reader）

[説明ページ]
https://tech.nkhn37.net/python-csv/#CSVreader
"""
import csv

with open('sample.csv', 'r', encoding='UTF-8') as file:
    data = []
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

print(data)
