"""urllib の基本的な使い方
リソースの取得をサーバーに要求する GET
クエリパラメータを含めてリクエストを送信する

[説明ページ]
https://tech.nkhn37.net/python-urllib-basic/
"""

import json
import urllib.parse
import urllib.request

# クエリパラメータを定義
params = {"key1": "value1", "key2": "value2"}
# クエリ文字列を作成する
query_string = urllib.parse.urlencode(params)

# httpbin へアクセスする場合は以下を有効化
# url = f"https://httpbin.org/get?{query_string}"

# Docker 環境で実行する場合は以下を有効化
url = f"http://localhost:8080/get?{query_string}"

with urllib.request.urlopen(url) as r:
    # 応答ボディの取得
    raw_data = r.read()

    # ステータスコード
    print(f"[status_code]:\n{r.status} {r.reason}\n")
    # ヘッダー
    print(f"[headers]:\n{r.getheaders()}\n")
    # 応答の生データ(バイナリ)
    print(f"[content]:\n{raw_data}\n")
    # 応答の文字列形式
    print(f"[text]:\n{raw_data.decode('utf-8')}\n")
    # 応答のJSON形式
    print(f"[json]:\n{json.loads(raw_data.decode('utf-8'))}\n")
