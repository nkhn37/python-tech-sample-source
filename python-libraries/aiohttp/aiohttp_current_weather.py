import asyncio
import configparser
import time
from pprint import pprint
from typing import Any

import aiohttp


async def get_current_weather_data(
    session: aiohttp.ClientSession,
    url: str,
    api_key: str,
    lat: float,
    lon: float,
    lang: str,
) -> dict[str, Any]:
    """現在の天気情報を取得する

    Args:
        session (aiohttp.ClientSession): セッション情報
        url (str): APIのURL
        api_key (str): APIキー
        lat (float): 緯度
        lon (float): 経度
        lang (str): 言語

    Returns:
        dict[str, Any]: 天気情報
    """

    # パラメータの設定
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "lang": lang,
    }

    # 非同期通信
    async with session.get(url, params=params) as response:
        # HTTPエラーが発生した場合に例外をスロー
        response.raise_for_status()

        # レスポンスをJSON形式で取得
        return await response.json()


async def main() -> None:
    """メインコルーチン"""
    # APIキーの読み込み
    config = configparser.ConfigParser()
    config.read("./config.ini", encoding="utf-8")
    api_key = config["API"]["key"]
    url = config["API"]["url_current_weather_data"]

    locations = [
        {"name": "sapporo", "lat": 43.065, "lon": 141.347},
        {"name": "tokyo", "lat": 35.689, "lon": 139.692},
        {"name": "nagoya", "lat": 35.180, "lon": 136.907},
        {"name": "osaka", "lat": 34.686, "lon": 135.520},
        {"name": "hiroshima", "lat": 34.397, "lon": 132.460},
        {"name": "okinawa", "lat": 26.212, "lon": 127.681},
    ]

    # タイムアウトの設定
    timeout = aiohttp.ClientTimeout(total=10)

    # 非同期セッションを作成
    async with aiohttp.ClientSession(timeout=timeout) as session:
        # タスクを作成
        tasks = [
            get_current_weather_data(
                session,
                url,
                api_key,
                loc["lat"],
                loc["lon"],
                "ja",
            )
            for loc in locations
        ]

        # タスクを実行して結果を取得
        results = await asyncio.gather(*tasks, return_exceptions=True)

        for result, loc in zip(results, locations):
            print(f"対象地域: {loc['name']}")

            if isinstance(result, Exception):
                print(f"エラーが発生しました: {result}")
            else:
                pprint(result)

            print("----------------------------------")


if __name__ == "__main__":
    # 時間計測の開始
    t = time.perf_counter()

    # asyncio.runを使用してメインコルーチンを実行
    asyncio.run(main())

    # 実行時間を表示
    print(f"実行時間: {time.perf_counter() - t:.5f} sec")
