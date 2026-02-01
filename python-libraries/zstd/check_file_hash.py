"""ファイルの SHA256 ハッシュ値を計算して比較

[説明ページ]
https://tech.nkhn37.net/python-zstd-basic/
"""

import hashlib


def sha256(path: str) -> str:
    """ハッシュ値計算用

    Args:
        path (str): 対象ファイルのパス

    Returns:
        str: SHA256 ハッシュ値（16 進文字列）
    """
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


if __name__ == "__main__":
    original_hash = sha256("sample.log")
    restored_hash = sha256("sample_restored.log")
    print(f"Original SHA256: {original_hash}")
    print(f"Restored SHA256: {restored_hash}")
    print("一致" if original_hash == restored_hash else "不一致")
