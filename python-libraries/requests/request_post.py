"""requestsの基本的な使い方
新しいリソースを作成する POST
application/jsonで送信　(json引数)

[説明ページ]
https://tech.nkhn37.net/python-requests-basic/#_POST
"""
import requests

# URLを指定
url = "http://httpbin.org/post"

# 登録データの作成
data = {"name": "Taro", "age": 30}

# データ登録リクエスト
r = requests.post(url, json=data)

# 応答結果の表示
print(f"text:\n {r.text}")
