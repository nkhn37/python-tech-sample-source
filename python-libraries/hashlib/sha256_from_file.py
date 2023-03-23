"""hashlibによるハッシュ化の基本
ファイルデータのハッシュ化 (Python バージョン3.11で追加)

[説明ページ]
https://tech.nkhn37.net/python-hashlib-basic/#_Python_311
"""
import hashlib


def main():
    filepath = "targetfile.txt"

    # ファイルを読み込んでハッシュ化
    with open(filepath, "rb") as f:
        h = hashlib.file_digest(f, "sha256")
    digest = h.hexdigest()
    print(digest)


if __name__ == "__main__":
    main()
