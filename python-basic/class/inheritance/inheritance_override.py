"""クラス基礎
継承におけるメソッドのオーバーライド

[説明ページ]
https://tech.nkhn37.net/python-class-inheritance/#i-2
"""


class Person:
    """人間クラス"""

    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    def say_myname(self):
        print(f"私の名前は、{self.last_name}{self.first_name}です。")


class Teacher(Person):
    """教師クラス"""

    def mywork(self):
        print(f"{self.last_name}{self.first_name}は教師として働いています。")

    # メソッドのオーバーライド
    def say_myname(self):
        print(f"私は、教師の{self.last_name}{self.first_name}です。")


def main():
    tanaka = Teacher("太郎", "田中")
    tanaka.say_myname()
    tanaka.mywork()


if __name__ == "__main__":
    main()
