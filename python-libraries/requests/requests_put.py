"""requestsの基本的な使い方
指定されたリソースを更新する PUT

[説明ページ]
https://tech.nkhn37.net/python-requests-basic/
"""

import requests

# httpbin へアクセスする場合は以下を有効化
# url = "https://httpbin.org/put"

# Docker 環境で実行する場合は以下を有効化
url = "http://localhost:8080/put"

# 更新データの作成
payload = {"name": "Miki", "age": 25}

# データ更新リクエスト
r = requests.put(url, json=payload)

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

print(r.headers.get("Content-Type"))
