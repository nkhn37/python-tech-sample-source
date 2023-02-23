"""クラス基礎
インスタンス変数の隠ぺい（カプセル化、マングリング）

[説明ページ]
https://tech.nkhn37.net/python-class-definition/#i-10
"""


class Person:
    """人間クラス"""

    kind = "human"

    def __init__(
        self, first_name=None, last_name=None, sex=None, birthday=None
    ):
        self.__first_name = first_name
        self.__last_name = last_name
        self._sex = sex
        self._birthday = birthday

    def say_myname(self):
        print(f"私の名前は、{self.__last_name} {self.__first_name} です。")


def main():
    tanaka = Person("太郎", "田中", "male", "2000/1/1")
    tanaka.say_myname()
    print(tanaka._sex)
    print(tanaka._birthday)
    # 隠ぺいされた変数へのアクセス
    # マングリングした名前
    # print(tanaka._Person__first_name)
    print(tanaka.__first_name)


if __name__ == "__main__":
    main()
