"""hashlibによるハッシュ化の基本
ログインを想定したハッシュ化の使用例

[説明ページ]
https://tech.nkhn37.net/python-hashlib-basic/#i-5
"""
import base64
import hashlib
import os

# ユーザーとパスワードのDB
db = {}
# saltの生成
salt = base64.b64encode(os.urandom(32))
# hash化の回数
iter_num = 100000


def get_digest(password: str):
    """パスワードのハッシュ値計算

    Args:
        password: パスワード文字列

    Returns:
        ハッシュ値
    """
    digest = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, iter_num
    ).hex()

    return digest


def is_login(user_name: str, password: str):
    """ログイン処理

    Args:
        user_name: ユーザー名
        password: パスワード

    Returns:
        ログイン結果
    """
    return get_digest(password) == db[user_name]


def main():
    user_name = "user01"
    user_password = "P@ssw0rd"

    digest = get_digest(user_password)
    db[user_name] = digest
    print(f"db: {db}\n")

    print(f"正常なログインの場合: {user_name} {user_password}")
    print(is_login(user_name, user_password))

    user_password_ng = "password"
    print(f"パスワード不正の場合: {user_name} {user_password_ng}")
    print(is_login(user_name, user_password_ng))


if __name__ == "__main__":
    main()
