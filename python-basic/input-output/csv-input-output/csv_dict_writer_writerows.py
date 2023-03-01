"""CSVファイルの入出力
DictWriterのwriterowsで複数行の辞書形式のデータをまとめて書き込む

[説明ページ]
https://tech.nkhn37.net/python-csv/#_writerows-2
"""
import csv

data = [
    {"id": 1, "name": "田中太郎", "date": "2021/1/1"},
    {"id": 2, "name": "伊藤洋子", "date": "2020/9/1"},
    {"id": 3, "name": "佐藤花子", "date": "2019/1/1"},
]

with open("out_dict_writerows.csv", "w", newline="", encoding="utf-8") as file:
    # ヘッダーの列名を指定
    field_names = ["id", "name", "date"]
    dict_writer = csv.DictWriter(file, fieldnames=field_names)

    # ヘッダーの書き込み
    dict_writer.writeheader()
    # writerowsでまとめて書き込み
    dict_writer.writerows(data)
