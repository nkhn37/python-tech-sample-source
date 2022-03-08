"""hashlibによるハッシュ化の基本
Salt(ソルト)とStretching(ストレッチング)を使った解読対策

[説明ページ]
https://tech.nkhn37.net/python-hashlib-basic/#SaltStretching
"""
import base64
import os
import hashlib

db = {}
salt = base64.b64encode(os.urandom(32))
print(f'salt: {salt}')


def get_digest(password):
    password = bytes(password, 'utf-8')
    # ソルト(salt)を付け加えてからハッシュ化
    digest = hashlib.sha256(salt + password).hexdigest()
    # ストレッチング(stretching)
    for _ in range(100000):
        digest = hashlib.sha256(bytes(digest, 'utf-8')).hexdigest()
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
