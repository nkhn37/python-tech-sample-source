"""requestsの基本的な使い方
例外処理 (raise_for_status)

[説明ページ]
https://tech.nkhn37.net/python-requests-basic/#i
"""

import requests
from requests.exceptions import HTTPError, RequestException

# httpbin へアクセスする場合は以下を有効化
# url = "https://httpbin.org/status/400"

# Docker 環境で実行する場合は以下を有効化
url = "http://localhost:8080/status/400"

try:
    # URLからデータを取得する
    r = requests.get(url)
    # HTTPエラーが発生した場合、例外を発生させる
    r.raise_for_status()

    # 応答結果の表示
    print(f"text:\n {r.text}")

except HTTPError as e:
    print(f"HTTPエラー: {e}")
except RequestException as e:
    print(f"通信エラー: {e}")
