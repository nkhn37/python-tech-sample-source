"""zstd によりデータを圧縮／解凍する基本
ストリーム圧縮の基本

[説明ページ]
https://tech.nkhn37.net/python-zstd-basic/
"""

from compression import zstd


def compress_file(
    src_path: str, dst_path: str, level: int | None = None
) -> None:
    """ファイルをストリーム圧縮する関数

    Args:
        src_path (str): 圧縮対象のファイルパス
        dst_path (str): 圧縮先ファイルパス
        level (int | None, optional): 圧縮レベル. デフォルトは None (zstd のデフォルトレベル 3 ).
    """
    # 1 MB のチャンクで処理
    chunk_size = 1024 * 1024

    # 対象ファイルを開いてストリーム圧縮
    with open(src_path, "rb") as f_in:
        # zstd で圧縮先ファイルを開く
        with zstd.open(dst_path, "wb", level=level) as f_out:
            # chunk_size ごとに読み込みながら圧縮して書き込み
            # ファイル末尾の b"" で停止するイテレータを使用
            for chunk in iter(lambda: f_in.read(chunk_size), b""):
                f_out.write(chunk)


if __name__ == "__main__":
    source_path = "sample.log"
    dest_path = "sample.log.zst"
    compress_file(source_path, dest_path)
