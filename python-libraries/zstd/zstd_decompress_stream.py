"""zstd によりデータを圧縮／解凍する基本
ストリーム解凍の基本

[説明ページ]
https://tech.nkhn37.net/python-zstd-basic/
"""

from compression import zstd


def decompress_file(src_path: str, dst_path: str) -> None:
    """zstd圧縮ファイルをストリーム解凍する関数

    Args:
        src_path (str): 対象ファイル（.zst）のパス
        dst_path (str): 解凍先のファイルパス
    """
    # 1 MB のチャンクで処理
    chunk_size = 1024 * 1024  # 1MB

    # zstd で圧縮元ファイルを開いてストリーム解凍
    with zstd.open(src_path, "rb") as f_in:
        # 解凍先ファイルを開く
        with open(dst_path, "wb") as f_out:
            for chunk in iter(lambda: f_in.read(chunk_size), b""):
                f_out.write(chunk)


if __name__ == "__main__":
    source_path = "sample.log.zst"
    dest_path = "sample_restored.log"
    decompress_file(source_path, dest_path)
