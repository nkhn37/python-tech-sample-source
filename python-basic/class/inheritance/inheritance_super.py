"""クラス基礎
superによる基底クラスのメソッド呼び出し

[説明ページ]
https://tech.nkhn37.net/python-class-inheritance/#super
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

    def __init__(self, first_name=None, last_name=None, subject=None):
        # 親クラスのコンストラクタの呼び出し
        super().__init__(first_name, last_name)
        # 自クラスの変数初期化
        self.subject = subject

    def mywork(self):
        print(f"{self.last_name}{self.first_name}は教師として働いています。")

    def say_myname(self):
        print(f"私は、{self.subject}教師の{self.last_name}" f"{self.first_name}です。")


def main():
    tanaka = Teacher("太郎", "田中", "英語")
    tanaka.say_myname()
    tanaka.mywork()


if __name__ == "__main__":
    main()
