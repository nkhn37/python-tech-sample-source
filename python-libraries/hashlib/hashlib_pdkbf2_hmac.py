"""hashlibによるハッシュ化の基本
pdkbf2_hmac関数を使った解読耐性のあるハッシュ値の取得

[説明ページ]
https://tech.nkhn37.net/python-hashlib-basic/#pdkbf2_hmac
"""
import base64
import os
import hashlib

db = {}
salt = base64.b64encode(os.urandom(32))
print(f'salt: {salt}')


def get_digest(password):
    digest = hashlib.pbkdf2_hmac(
        'sha256', bytes(password, 'utf-8'), salt, 100000).hex()
    return digest


def is_login(user_name, password):
    return get_digest(password) == db[user_name]


def main():
    user_name = 'user01'
    user_password = 'password01'

    digest = get_digest(user_password)
    db[user_name] = digest
    print(f'db：{db}')

    print(f'ログイン：{is_login(user_name, user_password)}')


if __name__ == '__main__':
    main()
