"""関数基礎
位置引数

[説明ページ]
https://tech.nkhn37.net/python-function-basic/#i-5
"""


def make_profile(first, last, birth):
    return {"first name": first, "last name": last, "birthday": birth}


if __name__ == "__main__":
    first_name = "Taro"
    last_name = "Python"
    birthday = "2021/1/1"

    # 位置引数にて指定
    profile = make_profile(first_name, last_name, birthday)
    print(profile)

    profile = make_profile(last_name, first_name, birthday)
    print(profile)
