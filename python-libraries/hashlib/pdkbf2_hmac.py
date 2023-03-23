"""hashlibによるハッシュ化の基本
pdkbf2_hmacを使った解読耐性のあるハッシュ値の取得

[説明ページ]
https://tech.nkhn37.net/python-hashlib-basic/#_pdkbf2_hmac
"""
import base64
import hashlib
import os

# saltの生成
salt = base64.b64encode(os.urandom(32))
# hash化の回数
iter_num = 100000


def main():
    password = "P@ssw0rd"
    print(password)

    # ハッシュ化
    digest = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, iter_num
    ).hex()
    print(digest)


if __name__ == "__main__":
    main()
