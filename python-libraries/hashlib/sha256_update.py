"""hashlibによるハッシュ化の基本
updateで複数対象を結合してハッシュ化

[説明ページ]
https://tech.nkhn37.net/python-hashlib-basic/#update
"""
import hashlib


def main():
    target_str1 = "sample01"
    target_str2 = "sample02"
    joined_str = target_str1 + target_str2
    print(target_str1)
    print(target_str2)
    print(joined_str, "\n")

    # updateで複数対象をつなげてハッシュ化
    h = hashlib.sha256()
    h.update(target_str1.encode("utf-8"))
    h.update(target_str2.encode("utf-8"))
    digest = h.hexdigest()
    print(digest)

    # 文字列を結合したもののハッシュ化と同じ
    digest = hashlib.sha256(joined_str.encode("utf-8")).hexdigest()
    print(digest)


if __name__ == "__main__":
    main()
