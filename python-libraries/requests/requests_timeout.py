"""requestsの基本的な使い方
タイムアウト設定

[説明ページ]
https://tech.nkhn37.net/python-requests-basic/
"""

import requests
from requests.exceptions import Timeout, RequestException

# httpbin へアクセスする場合は以下を有効化
# url = "https://httpbin.org/get"

# Docker 環境で実行する場合は以下を有効化
url = "http://localhost:8080/get"

try:
    # URLからデータを取得する
    # タプルで指定する場合は (接続タイムアウト, 読み取りタイムアウト)を指定
    # timeout=5.0 のようにすると、接続・読み取りともに5秒のタイムアウト設定となる
    r = requests.get(url, timeout=(3.0, 5.0))

    # 応答結果の表示
    print(f"text:\n {r.text}")

except Timeout as e:
    print(f"タイムアウトエラー: {e}")
except RequestException as e:
    print(f"通信エラー: {e}")
