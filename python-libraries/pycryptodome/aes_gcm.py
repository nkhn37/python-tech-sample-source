"""pycryptodomeによる暗号化・復号化
Advanced Encryption Standard (AES)を用いた共通鍵暗号方式
認証付き秘匿モード GCMを使用した方法

[説明ページ]
https://tech.nkhn37.net/python-pcryptodome-basic/#Advanced_Encryption_Standard_AES
"""
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def main():
    # 暗号化対象文字列
    plaintext = "pycryptodomeを用いた文字列の暗号化・復号化"
    print(plaintext)
    # 文字列をバイトに変換
    plaintext_byte = plaintext.encode("utf-8")

    print("\n===== 暗号化 =====")
    # キーの生成
    key = get_random_bytes(16)
    # nonceの生成
    nonce = get_random_bytes(12)
    # 暗号化用オブジェクトの準備
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    # 暗号化
    cipher_text, tag = cipher.encrypt_and_digest(plaintext_byte)
    print(f"暗号化文: {cipher_text}")
    print(f"TAG: {tag}")

    print("\n===== 復号化 =====")
    # 復号化用オブジェクトの準備
    cipher_dec = AES.new(key, AES.MODE_GCM, nonce=nonce)
    try:
        # 復号化
        decrypted_text = cipher_dec.decrypt_and_verify(cipher_text, tag)
        print(decrypted_text.decode())
    except (ValueError, KeyError) as ex:
        print(f"不正な復号 {ex}")


if __name__ == "__main__":
    main()
