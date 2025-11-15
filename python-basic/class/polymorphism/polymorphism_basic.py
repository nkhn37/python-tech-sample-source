"""クラス基礎
ポリモーフィズムと抽象クラス、抽象メソッド

[説明ページ]
https://tech.nkhn37.net/python-class-polymorphism/
"""

import abc


class Person(abc.ABC):
    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    def say_myname(self) -> None:
        print(f"私の名前は、{self.__name}です。")

    @abc.abstractmethod
    def mywork(self) -> None:
        ...
        # pass でもよい


class Teacher(Person):
    def __init__(self, name: str, subject: str) -> None:
        super().__init__(name)
        self.__subject = subject

    @property
    def subject(self) -> str:
        return self.__subject

    @subject.setter
    def subject(self, value: str) -> None:
        self.__subject = value

    def mywork(self) -> None:
        print(f"私の仕事は、{self.__subject}の教師です。")


class Doctor(Person):
    def __init__(self, name: str, medical_speciality: str) -> None:
        super().__init__(name)
        self.__medical_speciality = medical_speciality

    @property
    def medical_speciality(self) -> str:
        return self.__medical_speciality

    @medical_speciality.setter
    def medical_speciality(self, value: str) -> None:
        self.__medical_speciality = value

    def mywork(self) -> None:
        print(f"私の仕事は、{self.__medical_speciality}の医者です。")


def introduction(person: Person) -> None:
    """Person 型の引数を受け取る"""
    print("=== introduction ===")
    person.say_myname()
    person.mywork()


def main():
    person1 = Teacher("田中太郎", "英語")
    person1.mywork()
    introduction(person1)

    print("==================================")

    person2 = Doctor("鈴木一郎", "内科")
    person2.mywork()
    introduction(person2)


if __name__ == "__main__":
    main()
