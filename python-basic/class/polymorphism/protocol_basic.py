"""クラス基礎
構造的部分型を使ったインターフェース

[説明ページ]
https://tech.nkhn37.net/python-class-polymorphism/
"""

from typing import Protocol


# Protocol: 構造的部分型を使ったインターフェース
class Person(Protocol):
    @property
    def name(self) -> str: ...

    @name.setter
    def name(self, value: str) -> None: ...

    def say_myname(self) -> None: ...

    def mywork(self) -> None: ...


# Teacher クラス (Person は継承しない)
class Teacher:
    def __init__(self, name: str, subject: str) -> None:
        self._name = name
        self._subject = subject

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    def say_myname(self) -> None:
        print(f"私の名前は、{self._name}です。")

    def mywork(self) -> None:
        print(f"私の仕事は、{self._subject}の教師です。")


# Doctor クラス (Person は継承しない)
class Doctor:
    def __init__(self, name: str, medical_speciality: str) -> None:
        self._name = name
        self._medical_speciality = medical_speciality

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    def say_myname(self) -> None:
        print(f"私の名前は、{self._name}です。")

    def mywork(self) -> None:
        print(f"私の仕事は、{self._medical_speciality}の医者です。")


def introduction(person: Person) -> None:
    """Person 型の引数を受け取る"""
    print("=== introduction ===")
    person.say_myname()
    person.mywork()


def main() -> None:
    person1 = Teacher("田中太郎", "英語")
    person1.mywork()
    introduction(person1)

    print("==================================")

    person2 = Doctor("鈴木一郎", "内科")
    person2.mywork()
    introduction(person2)


if __name__ == "__main__":
    main()
