import configparser
import os
from pprint import pprint

from rest_api import call_rest_api


def main():
    # REST API のエンドポイント URL をconfig.ini から読み込む
    config = configparser.ConfigParser()
    config.read("./config.ini")
    url_direct_geocoding = config["API"]["url_direct_geocoding"]

    # APIキーは環境変数から取得
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("APIキーが環境変数に設定されていません。")
        return

    # ===== 場所情報を取得
    params = {
        "q": "tokyo",
        "appid": api_key,
    }

    try:
        # データの取得
        response = call_rest_api(
            method="GET",
            url=url_direct_geocoding,
            params=params,
            timeout=5,
        )
    except Exception as ex:
        print(ex)
        return

    # レスポンスを表示
    pprint(response)


if __name__ == "__main__":
    main()
