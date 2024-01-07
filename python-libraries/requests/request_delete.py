"""requestsの基本的な使い方
指定されたリソースをサーバーから削除する DELETE

[説明ページ]
https://tech.nkhn37.net/python-requests-basic/#_DELETE
"""
import requests

# URLを指定
url = "http://httpbin.org/delete"

# 削除データの指定
data = {"id": 123}

# データ削除リクエスト
r = requests.delete(url, json=data)

# 応答結果の表示
print(f"text:\n {r.text}")
