"""クラス基礎
クラスの定義と使い方

[説明ページ]
https://tech.nkhn37.net/python-class-definition/#Python-2
"""


class Person:
    """人間クラス"""

    kind = "human"

    def __init__(
        self, first_name=None, last_name=None, sex=None, birthday=None
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.birthday = birthday

    def say_myname(self):
        print(f"私の名前は、{self.last_name} {self.first_name} です。")

    @staticmethod
    def say_hello(greeting):
        print(greeting)

    @classmethod
    def get_kind(cls):
        return cls.kind

    def __del__(self):
        print(f"{self.last_name} {self.first_name} : delete")


def main():
    # クラスからインスタンスを生成
    tanaka = Person("太郎", "田中", "male", "2000/1/1")
    # クラスのメソッドを呼び出し
    tanaka.say_hello("こんにちは")
    tanaka.say_myname()
    print("---")

    # 別のインスタンスを生成
    sato = Person("愛子", "佐藤", "female", "2001/9/1")
    sato.say_hello("こんばんは")
    sato.say_myname()
    print("---")

    # クラスメソッドの呼び出し
    print(Person.get_kind())
    print("---")


if __name__ == "__main__":
    main()
