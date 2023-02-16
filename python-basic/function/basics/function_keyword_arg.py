"""関数基礎
キーワード引数

[説明ページ]
https://tech.nkhn37.net/python-function-basic/#i-6
"""


def make_profile(first, last, birth):
    return {"first name": first, "last name": last, "birthday": birth}


if __name__ == "__main__":
    first_name = "Taro"
    last_name = "Python"
    birthday = "2021/1/1"

    # キーワード引数にて指定
    profile = make_profile(birth=birthday, last=last_name, first=first_name)
    print(profile)
