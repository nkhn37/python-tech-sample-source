"""json モジュールの基本
JSON 形式ファイルの書き込み時のインデント設定
indent 引数

※ dumps 関数でも同様の引数が使用可能

[説明ページ]
https://tech.nkhn37.net/python-json-dump-load
"""

import json

# データを用意
data = {
    "data": [
        {"id": 1, "name": "太郎"},
        {"id": 2, "name": "はるか"},
        {"id": 3, "name": "さくら"},
    ]
}

# JSON ファイルへの書き込み (デフォルト: indent=None)
with open("test_indent_none.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)

# JSON ファイルへの書き込み (indent=2)
with open("test_indent_2.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
