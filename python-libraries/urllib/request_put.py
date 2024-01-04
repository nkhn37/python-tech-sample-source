"""urllibの基本的な使い方
指定されたリソースを更新する PUT

[説明ページ]
https://tech.nkhn37.net/python-urllib-basic/#_PUT
"""
import json
import urllib.request

# URLを指定
url = "http://httpbin.org/put"

# 更新データの作成
data = {"name": "Miki", "age": 25}
data = json.dumps(data).encode("utf-8")
# ヘッダーの設定
headers = {"Content-Type": "application/json"}

# リクエストの作成
request = urllib.request.Request(url, data=data, headers=headers, method="PUT")

with urllib.request.urlopen(request) as response:
    # レスポンスからデータを取得
    result = json.loads(response.read().decode("utf-8"))

print(result)
