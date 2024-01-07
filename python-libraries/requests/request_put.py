"""requestsの基本的な使い方
指定されたリソースを更新する PUT

[説明ページ]
https://tech.nkhn37.net/python-requests-basic/#_PUT
"""
import requests

# URLを指定
url = "http://httpbin.org/put"

# 更新データの作成
data = {"name": "Miki", "age": 25}

# データ更新リクエスト
r = requests.put(url, json=data)

# 応答結果の表示
print(f"text:\n {r.text}")
