"""入出力基礎
CSVファイルの入出力（writer）

[説明ページ]
https://tech.nkhn37.net/python-csv/#CSVwriterwriterows
"""
import csv

data = [['1', '田中太郎', '2021/1/1'],
        ['2', '伊藤洋子', '2020/9/1'],
        ['3', '佐藤花子', '2019/1/1']]

with open('sample_out.csv', 'w', newline='', encoding='UTF-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)
