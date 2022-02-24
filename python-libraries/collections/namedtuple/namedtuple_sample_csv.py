"""Collectionsモジュール
名前付きタプル namedtupleの使いどころ
csvファイルの読み込みに使用する

[説明ページ]
https://tech.nkhn37.net/python-collections-namedtuple/#csv
"""
import collections
import csv

# CSVファイルを作成して保存する
with open('temp.csv', 'w', newline='', encoding='UTF-8') as csv_write:
    fields = ['index', 'value1', 'value2', 'value3']
    writer = csv.DictWriter(csv_write, fieldnames=fields)

    writer.writeheader()
    for i in range(1, 6):
        writer.writerow({'index': i, 'value1': f'val1-{i}',
                         'value2': f'val2-{i}', 'value3': f'val3-{i}'})

# CSVファイルをnamedtupleに読み込む
with open('temp.csv', 'r', encoding='UTF-8') as csv_read:
    csv_reader = csv.reader(csv_read)

    data = []
    # namedtupleを定義する（CSVの1行目を列名として定義）
    record = collections.namedtuple('record', next(csv_reader))
    # CSVのレコードを順次読み込む
    for row in csv_reader:
        # namedtupleで1行を読み込む
        d = record._make(row)
        data.append(d)

print(data)
# 1行目のデータに列名でアクセスする
print(data[0].index)
print(data[0].value1)
print(data[0].value2)
print(data[0].value3)
