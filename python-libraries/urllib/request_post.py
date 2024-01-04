"""urllibの基本的な使い方
新しいリソースを作成する POST

[説明ページ]
https://tech.nkhn37.net/python-urllib-basic/#_POST
"""
import json
import urllib.request

# URLを指定
url = "http://httpbin.org/post"

# 登録データの作成
data = {"name": "Taro", "age": 30}
data = json.dumps(data).encode("utf-8")
# ヘッダーの設定
headers = {"Content-Type": "application/json"}

# リクエストの作成
request = urllib.request.Request(
    url, data=data, headers=headers, method="POST"
)

with urllib.request.urlopen(request) as response:
    # レスポンスからデータを取得
    result = json.loads(response.read().decode("utf-8"))

print(result)
