from typing import Any

import requests


def call_rest_api(
    method: str,
    url: str,
    params: dict[str, Any],
    timeout: int = 5,
) -> dict[str, Any]:
    """REST API を呼び出す

    Args:
        method (str): HTTP メソッド (例: "GET", "POST")
        url (str): API のエンドポイント URL
        params (dict[str, Any]): クエリパラメータ
        timeout (int, optional): タイムアウト時間 (秒). Defaults to 5.

    Raises:
        RuntimeError: API リクエスト中にエラーが発生した場合

    Returns:
        dict[str, Any]: API レスポンスの JSON データ
    """
    try:
        # APIリクエストの送信
        response = requests.request(
            method=method.upper(),
            url=url,
            params=params,
            timeout=timeout,
        )

        # HTTPエラーが発生した場合に例外をスロー
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as ex:
        # エラーが発生した場合は、例外をスロー
        raise RuntimeError(f"API リクエスト中にエラーが発生しました: {ex}") from ex
