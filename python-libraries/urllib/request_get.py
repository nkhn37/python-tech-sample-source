"""urllibの基本的な使い方
リソースの取得をサーバーに要求する GET
基本的な使い方

[説明ページ]
https://tech.nkhn37.net/python-urllib-basic/#_GET
"""
import json
import urllib.request

# URLを指定
url = "http://httpbin.org/get"

with urllib.request.urlopen(url) as response:
    # レスポンスからデータを取得
    data = json.loads(response.read().decode("utf-8"))

print(data)
