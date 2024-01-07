"""requestsの基本的な使い方
リソースの取得をサーバーに要求する GET
クエリパラメータを含めてリクエストを送信する

[説明ページ]
https://tech.nkhn37.net/python-requests-basic/#_GET
"""
import requests

# URLを指定
url = "http://httpbin.org/get"

# クエリパラメータを定義
params = {"key1": "value1", "key2": "value2"}

r = requests.get(url, params=params)

# 応答結果の表示
print(f"text:\n {r.text}")
