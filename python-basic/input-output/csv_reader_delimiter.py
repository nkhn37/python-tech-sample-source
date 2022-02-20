"""入出力基礎
CSVファイルの入出力（reader, 区切り文字の指定）

[説明ページ]
https://tech.nkhn37.net/python-csv/#delimiter
"""
import csv

with open('sample_tab.csv', 'r', encoding='UTF-8') as file:
    data = []
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        data.append(row)

print(data)
