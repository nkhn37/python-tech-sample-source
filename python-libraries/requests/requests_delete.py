"""requestsの基本的な使い方
指定されたリソースをサーバーから削除する DELETE

[説明ページ]
https://tech.nkhn37.net/python-requests-basic/
"""

import requests

# httpbin へアクセスする場合は以下を有効化
# url = "https://httpbin.org/delete"

# Docker 環境で実行する場合は以下を有効化
url = "http://localhost:8080/delete"

# 削除データの指定
payload = {"id": 123}

# データ削除リクエスト
r = requests.delete(url, json=payload)

# ステータスコード
print(f"[status_code]:\n{r.status_code} {r.reason}\n")
# ヘッダー
print(f"[headers]:\n{r.headers}\n")
# 応答の生データ(バイナリ)
print(f"[content]:\n{r.content}\n")
# 応答の文字列形式
print(f"[text]:\n{r.text}\n")
# 応答のJSON形式
print(f"[json]:\n{r.json()}\n")
