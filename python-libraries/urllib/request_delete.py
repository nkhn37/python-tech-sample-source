"""urllibの基本的な使い方
指定されたリソースをサーバーから削除する DELETE

[説明ページ]
https://tech.nkhn37.net/python-urllib-basic/#_DELETE
"""
import json
import urllib.request

# URLを指定
url = "http://httpbin.org/delete"

# 削除データの指定
data = {"id": 123}
data = json.dumps(data).encode("utf-8")
# ヘッダーの設定
headers = {"Content-Type": "application/json"}

# リクエストの作成
request = urllib.request.Request(
    url, data=data, headers=headers, method="DELETE"
)

with urllib.request.urlopen(request) as response:
    # レスポンスからデータを取得
    result = json.loads(response.read().decode("utf-8"))

print(result)
