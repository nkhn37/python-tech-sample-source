"""hashlibによるハッシュ化の基本
基本的な使い方 SHA-256

[説明ページ]
https://tech.nkhn37.net/python-hashlib-basic/#i-4
"""
import hashlib


def main():
    password = "P@ssw0rd"
    print(password)

    # SHA-256でハッシュ化
    digest = hashlib.sha256(password.encode("utf-8")).hexdigest()
    print(digest)


if __name__ == "__main__":
    main()
