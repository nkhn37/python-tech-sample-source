"""json モジュールの基本
JSON 形式ファイルの書き込み時の文字エンコード設定
ensure_ascii 引数

※ dumps 関数でも同様の引数が使用可能

[説明ページ]
https://tech.nkhn37.net/python-json-dump-load
"""

import json

# データを用意（日本語を含む）
data = {
    "data": [
        {"id": 1, "name": "太郎"},
        {"id": 2, "name": "はるか"},
        {"id": 3, "name": "さくら"},
    ]
}

# JSON ファイルへの書き込み（デフォルト: ensure_ascii=True）
with open("test_ensure_ascii_true.json", "w", encoding="utf-8") as f:
    json.dump(data, f)

# JSON ファイルへの書き込み（ensure_ascii=False）
with open("test_ensure_ascii_false.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)
