"""urllibの基本的な使い方
リソースの取得をサーバーに要求する GET
クエリパラメータを含めてリクエストを送信する

[説明ページ]
https://tech.nkhn37.net/python-urllib-basic/#_GET
"""
import json
import urllib.parse
import urllib.request

# クエリパラメータを定義
params = {"key1": "value1", "key2": "value2"}
# クエリ文字列を作成する
query_string = urllib.parse.urlencode(params)
# クエリパラメータを含めたURLを作成
url = f"http://httpbin.org/get?{query_string}"
print(url, "\n")

with urllib.request.urlopen(url) as response:
    # レスポンスからデータを取得
    data = json.loads(response.read().decode("utf-8"))

print(data)
