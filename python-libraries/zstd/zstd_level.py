"""zstd によりデータを圧縮／解凍する基本
圧縮レベルの違いによる圧縮率の変化を確認

[説明ページ]
https://tech.nkhn37.net/python-zstd-basic/
"""

from compression import zstd
from datetime import datetime, timedelta

# ログ風の大きなテストデータを生成
lines = []
start = datetime.now()
num = 100_000

for i in range(num):
    ts = start + timedelta(seconds=i % 60)
    lines.append(
        f"{ts.strftime('%Y-%m-%dT%H:%M:%S')} INFO user_id={i%10000} action=click page=/items/{i%500}\n"
    )
data = "".join(lines).encode("utf-8")


def report_compression_results(level, compressed, original_size):
    """圧縮結果を表示する関数"""

    compressed_size = len(compressed)
    compression_percent = (compressed_size / original_size) * 100

    print(
        f"Level {level:>2}:"
        f" 圧縮後サイズ: {compressed_size:>10,} バイト,"
        f" 圧縮後サイズ比: {compression_percent:>6.2f} %"
    )


original_size = len(data)
print(f"元のサイズ: {original_size:,} バイト")

# level=1 (高速圧縮)
compressed_level1 = zstd.compress(data, level=1)
report_compression_results(1, compressed_level1, original_size)

# zstd を使ってデータを圧縮 (level指定による変化を確認)
# デフォルトは level=3
compressed = zstd.compress(data)
report_compression_results(3, compressed, original_size)

# level=10 (中程度の圧縮)
compressed_level10 = zstd.compress(data, level=10)
report_compression_results(10, compressed_level10, original_size)

# level=22 (最大の設定、最高圧縮、非常に遅い)
compressed_level22 = zstd.compress(data, level=22)
report_compression_results(22, compressed_level22, original_size)
