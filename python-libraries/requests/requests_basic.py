"""requestsの基本的な使い方
requests 関数の基本的な使い方

[説明ページ]
https://tech.nkhn37.net/python-requests-basic/
"""

import requests

# ===== URLを指定 (GET)
# url = "http://httpbin.org/get"
url = "http://localhost:8080/get"

# データ取得リクエスト
r = requests.request("GET", url)
# ステータスコード
print(f"[GET] {r.status_code} {r.reason}")

# ===== URLを指定 (POST)
# url = "http://httpbin.org/post"
url = "http://localhost:8080/post"

# 登録データの作成
payload = {"name": "Taro", "age": 30}
# データ登録リクエスト
r = requests.request("POST", url, json=payload)
# ステータスコード
print(f"[POST] {r.status_code} {r.reason}")

# ===== URLを指定 (PUT)
# url = "http://httpbin.org/put"
url = "http://localhost:8080/put"

# 更新データの作成
payload = {"name": "Miki", "age": 25}
# データ更新リクエスト
r = requests.request("PUT", url, json=payload)
# ステータスコード
print(f"[PUT] {r.status_code} {r.reason}")

# ===== URLを指定 (DELETE)
# url = "http://httpbin.org/delete"
url = "http://localhost:8080/delete"

# 削除データの指定
payload = {"id": 123}
# データ削除リクエスト
r = requests.request("DELETE", url, json=payload)
# ステータスコード
print(f"[DELETE] {r.status_code} {r.reason}")
