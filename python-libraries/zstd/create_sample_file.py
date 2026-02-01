"""ログ風のサンプルファイルを作成するスクリプト

[説明ページ]
https://tech.nkhn37.net/python-zstd-basic/
"""

from datetime import datetime, timedelta


def create_sample_log_file(filepath: str, size_mb: int = 10) -> None:
    """指定サイズ(MB) 以下に収まるログ風のサンプルファイルを作成する関数

    Args:
        filepath (str): 作成するファイルのパス
        size_mb (int, optional): 目標サイズ(MB). デフォルトは10MB.
    """
    target_size = size_mb * 1024 * 1024  # MB をバイトに変換
    start = datetime.now()

    written = 0
    i = 0

    with open(filepath, "wb") as f:
        while written < target_size:
            ts = start + timedelta(seconds=i % 60)
            line = (
                f"{ts:%Y-%m-%dT%H:%M:%S} INFO user_id={i%10000} "
                f"action=click page=/items/{i%500}\n"
            ).encode("utf-8")

            # 書き込み後にサイズ超過しそうなら終了
            if written + len(line) > target_size:
                break

            f.write(line)
            written += len(line)
            i += 1

    print(f"Created: {filepath}")
    print(f"Target : {size_mb} MB ({target_size:,} bytes)")
    print(f"Actual : {written / 1024 / 1024:.2f} MB ({written:,} bytes)")
    print(f"Lines  : {i:,}")


if __name__ == "__main__":
    path = "sample.log"
    create_sample_log_file(path, size_mb=100)
