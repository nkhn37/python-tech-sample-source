"""hashlibによるハッシュ化の基本
基本的な使い方

[説明ページ]
https://tech.nkhn37.net/python-hashlib-basic/#i-4
"""
import hashlib

db = {}


def get_digest(password):
    password = bytes(password, 'utf-8')
    digest = hashlib.sha256(password).hexdigest()
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
