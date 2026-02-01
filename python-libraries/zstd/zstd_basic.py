"""zstd によりデータを圧縮／解凍する基本
基本的な使い方

[説明ページ]
https://tech.nkhn37.net/python-zstd-basic/
"""

from compression import zstd

# 圧縮／解凍対象のデータ
data = "Zstandard 圧縮テストデータ".encode("utf-8")

# zstd を使ってデータを圧縮
compressed = zstd.compress(data)

# zstd を使ってデータを解凍
restored = zstd.decompress(compressed)
print(f"解凍後のデータ: {restored.decode('utf-8')}")
