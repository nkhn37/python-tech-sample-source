"""jsonモジュール
Python辞書とJSON形式文字列間での変換 dumps, loads

[説明ページ]
https://tech.nkhn37.net/python-json-dump-load/#PythonJSON_dumps_loads
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

# JSON形式文字列への変換
json_data = json.dumps(data)
print(json_data)
print(type(json_data), "\n")

# JSON形式文字列を辞書へ変換
data_dic = json.loads(json_data)
print(data_dic)
print(type(data_dic))
