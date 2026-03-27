import configparser
import os
from pprint import pprint

from rest_api import call_rest_api


def main():
    # REST API のエンドポイント URL を config.ini から読み込む
    config = configparser.ConfigParser()
    config.read("./config.ini")
    url_current_weather_data = config["API"]["url_current_weather_data"]

    # APIキーは環境変数から取得
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("APIキーが環境変数に設定されていません。")
        return

    # 東京 緯度: 35.6894 経度: 139.6917
    params = {
        "lat": 35.6894,
        "lon": 139.6917,
        "appid": api_key,
        "units": "metric",
        "lang": "ja",
    }

    try:
        # データの取得
        response = call_rest_api(
            method="GET",
            url=url_current_weather_data,
            params=params,
            timeout=5,
        )
    except Exception as ex:
        print(ex)
        return

    #  レスポンスを表示
    pprint(response)


if __name__ == "__main__":
    main()
