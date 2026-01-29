"""json モジュールの基本
変換できない型のデフォルト処理の指定
default 引数

※ dumps 関数でも同様の引数が使用可能

[説明ページ]
https://tech.nkhn37.net/python-json-dump-load
"""

import json
from datetime import datetime, timezone, timedelta

# データを用意
data = {
    "id": 1,
    # datetime 型はそのままでは変換できない
    "created_at": datetime.now(timezone(timedelta(hours=9))),
    # set 型もそのままでは変換できない
    "tags": {"python", "json", "example"},
    # bytes 型もそのままでは変換できない
    "raw_data": b"binarydata",
}

# JSON ファイルへの書き込み (変換できない型を文字列に変換)
with open("test_default.json", "w", encoding="utf-8") as f:
    json.dump(
        data,
        f,
        ensure_ascii=False,
        indent=2,
        # default 引数で変換できない型を文字列に変換
        default=str,
    )
