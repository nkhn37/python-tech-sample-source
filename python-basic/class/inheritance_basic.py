"""クラス基礎
クラスの継承の基本

[説明ページ]
https://tech.nkhn37.net/python-class-inheritance/#i
"""


class Person(object):
    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    def say_myname(self):
        print(f'私の名前は、{self.last_name}{self.first_name}です。')


class Teacher(Person):
    def mywork(self):
        print(f'{self.last_name}{self.first_name}は教師として働いています。')


def main():
    tanaka = Teacher('太郎', '田中')
    # 親クラスのメソッドの呼び出し
    tanaka.say_myname()
    # 自分のクラスのメソッドの呼び出し
    tanaka.mywork()


if __name__ == '__main__':
    main()
