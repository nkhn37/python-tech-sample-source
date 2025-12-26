"""urllib の基本的な使い方
リソースの取得をサーバーに要求する GET
基本的な使い方

[説明ページ]
https://tech.nkhn37.net/python-urllib-basic/
"""

import json
import urllib.request

# httpbin へアクセスする場合は以下を有効化
# url = "https://httpbin.org/get"

# Docker 環境で実行する場合は以下を有効化
url = "http://localhost:8080/get"

with urllib.request.urlopen(url) as r:
    # 応答ボディの取得 (read() は一度しか呼び出せないため注意)
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
