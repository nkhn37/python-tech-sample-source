"""クラス基礎
ポリモーフィズムと抽象クラス、抽象メソッド

[説明ページ]
https://tech.nkhn37.net/python-class-polymorphism/
"""
import abc


class Person(abc.ABC):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @staticmethod
    def say_myname(self):
        print(f'私の名前は、{self.__name}です。')

    @abc.abstractmethod
    def mywork(self):
        pass


class Teacher(Person):
    def __init__(self, subject):
        self.__subject = subject

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        self.__subject = value

    def mywork(self):
        print(f'私の仕事は、{self.__subject}の教師です。')


class Doctor(Person):
    def __init__(self, medical_speciality):
        self.__medical_speciality = medical_speciality

    @property
    def medical_speciality(self):
        return self.__medical_speciality

    @medical_speciality.setter
    def medical_speciality(self, value):
        self.__medical_speciality = value

    def mywork(self):
        print(f'私の仕事は、{self.__medical_speciality}の医者です。')


def main():
    person1 = Teacher('英語')
    person1.mywork()
    print('===')
    person2 = Doctor('内科')
    person2.mywork()


if __name__ == '__main__':
    main()
