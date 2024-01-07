"""requestsの基本的な使い方
リソースの取得をサーバーに要求する GET
基本的な使い方

[説明ページ]
https://tech.nkhn37.net/python-requests-basic/#_GET
"""
import requests

# URLを指定
url = "http://httpbin.org/get"

# データを取得する
r = requests.get(url)

# 応答の生データ(バイナリ)
print(f"content:\n {r.content}")
# ステータスコード
print(f"status_code:\n {r.status_code}")
# ヘッダー
print(f"headers:\n {r.headers}")
# 応答の文字列
print(f"text:\n {r.text}")
# 応答のJSON形式
print(f"json:\n {r.json()}")
