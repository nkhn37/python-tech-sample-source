"""json モジュールの基本
変換できない型のデフォルト処理の指定
default 引数（型ごとに処理を分ける例）

※ dumps 関数でも同様の引数が使用可能

[説明ページ]
https://tech.nkhn37.net/python-json-dump-load
"""

import base64
import json
from datetime import datetime, timezone, timedelta

# from zoneinfo import ZoneInfo


def default_serializer(obj):
    """変換できない型ごとに処理を分ける例"""

    if isinstance(obj, datetime):
        # datetime 型は ISO 形式の文字列に変換 (タイムゾーンを日本に設定)
        return obj.astimezone(timezone(timedelta(hours=9))).isoformat()

        # または ZoneInfo を使う場合 (ただし、pip install tzdata が必要な場合あり)
        # return obj.astimezone(ZoneInfo("Asia/Tokyo")).isoformat()

    elif isinstance(obj, set):
        # set 型はリストに変換
        return list(obj)

    elif isinstance(obj, bytes):
        # bytes 型は base64 エンコードして文字列に変換
        return base64.b64encode(obj).decode("utf-8")

    else:
        raise TypeError(f"Type {type(obj)} not serializable")


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
with open("test_default_serializer.json", "w", encoding="utf-8") as f:
    json.dump(
        data,
        f,
        ensure_ascii=False,
        indent=2,
        # default 引数で変換できない型ごとに処理を分ける関数を指定
        default=default_serializer,
    )
