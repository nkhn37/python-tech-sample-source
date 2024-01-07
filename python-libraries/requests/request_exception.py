"""requestsの基本的な使い方
例外処理とタイムアウト設定

[説明ページ]
https://tech.nkhn37.net/python-requests-basic/#i
"""
import requests
from requests.exceptions import HTTPError, Timeout

# URLを指定
url = "http://httpbin.org/get"
# # URL 400 Bad Requestのステータスコード
# url = "http://httpbin.org/status/400"

try:
    # URLからデータを取得する (タイムアウト)
    r = requests.get(url, timeout=1)
    r.raise_for_status()
    # 応答結果の表示
    print(f"text:\n {r.text}")

except HTTPError as http_err:
    print(f"HTTPエラー発生: {http_err}")
except Timeout as timeout_err:
    print(f"タイムアウトエラー発生: {timeout_err}")
except Exception as err:
    print(f"エラー発生: {err}")
