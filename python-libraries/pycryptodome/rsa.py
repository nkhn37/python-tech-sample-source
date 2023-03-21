"""pycryptodomeによる暗号化・復号化
RSAを用いた公開鍵暗号方式　暗号化と復号化

[説明ページ]
https://tech.nkhn37.net/python-pcryptodome-basic/#RSA
"""
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


def main():
    # 暗号化対象文字列
    plaintext = "pycryptodomeを用いた文字列の暗号化・復号化"
    print(plaintext)
    # 文字列をバイトに変換
    plaintext_byte = plaintext.encode("utf-8")

    print("\n===== 暗号化 =====")
    # 公開鍵の読み込み
    with open("public.pem", "r") as f:
        public_key = RSA.import_key(f.read())

    # 暗号化用オブジェクトの準備
    cipher = PKCS1_OAEP.new(public_key)
    cipher_text = cipher.encrypt(plaintext_byte)
    print(f"暗号化文: {cipher_text}")

    print("\n===== 復号化 =====")
    # 秘密鍵の読み込み
    with open("private.pem", "r") as f:
        private_key = RSA.import_key(f.read())

    # 復号化用オブジェクトの準備
    cipher_dec = PKCS1_OAEP.new(private_key)
    decrypted_text = cipher_dec.decrypt(cipher_text)
    print(decrypted_text.decode())


if __name__ == "__main__":
    main()
