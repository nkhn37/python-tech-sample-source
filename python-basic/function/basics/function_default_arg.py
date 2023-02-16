"""関数基礎
引数のデフォルト値の指定方法

[説明ページ]
https://tech.nkhn37.net/python-function-basic/#i-7
"""


# デフォルト値を指定
def make_profile(first=None, last=None, birth=None):
    return {"first name": first, "last name": last, "birthday": birth}


if __name__ == "__main__":
    first_name = "Taro"
    last_name = "Python"
    birthday = "2021/1/1"

    # キーワード引数にて指定
    profile = make_profile(first=first_name, birth=birthday)
    print(profile)

    profile = make_profile(first=first_name, last=last_name, birth=birthday)
    print(profile)
