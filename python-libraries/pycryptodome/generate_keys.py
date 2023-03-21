"""pycryptodomeによる暗号化・復号化
RSAを用いた公開鍵暗号方式 キーの生成

[説明ページ]
https://tech.nkhn37.net/python-pcryptodome-basic/#RSA
"""
from Crypto.PublicKey import RSA


def main():
    # キーペアの生成
    key = RSA.generate(2048)
    # 秘密鍵
    private_key = key.export_key()
    with open("private.pem", "wb") as f:
        f.write(private_key)

    # 公開鍵の生成
    public_key = key.public_key().export_key()
    with open("public.pem", "wb") as f:
        f.write(public_key)


if __name__ == "__main__":
    main()
