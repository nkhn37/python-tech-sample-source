"""json モジュールの基本
JSON 形式ファイルの読み込み / 書き込み方法 dump, load

[説明ページ]
https://tech.nkhn37.net/python-json-dump-load
"""

import json

# データを用意
data = {
    "data": [
        {"id": 1, "name": "Taro"},
        {"id": 2, "name": "Haruka"},
        {"id": 3, "name": "Sakura"},
    ]
}

# JSON ファイルへの書き込み
with open("test.json", "w", encoding="utf-8") as f:
    json.dump(data, f)

# JSON ファイルの読み込み
with open("test.json", "r", encoding="utf-8") as f:
    data_r = json.load(f)
    print(data_r)
    print(type(data_r))
