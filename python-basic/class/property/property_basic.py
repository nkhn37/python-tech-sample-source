"""クラス基礎
クラスのプロパティ（property）の使い方

[説明ページ]
https://tech.nkhn37.net/python-class-property/#property-2
"""


class Person:
    def __init__(self, first_name=None, last_name=None, age=None):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def age(self):
        return self.__age

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @age.setter
    def age(self, value):
        if value >= 0:
            self.__age = value
        else:
            raise ValueError(
                "Only values greater than or equal to 0 are allowed."
            )

    def myname(self):
        print(f"私の名前は、{self.__last_name}{self.__first_name}、{self.__age}歳です。")


def main():
    person1 = Person("太郎", "田中", 20)
    print(person1.first_name)
    print(person1.last_name)
    print(person1.age)
    person1.myname()
    print("===")

    person1.first_name = "次郎"
    person1.last_name = "佐藤"
    person1.age = 15
    print(person1.first_name)
    print(person1.last_name)
    print(person1.age)
    person1.myname()


if __name__ == "__main__":
    main()
