from csv_utility import CsvSerializable
from typing import override


class Student(CsvSerializable):
    def __init__(self, name: str | None = None, surname: str | None = None, group: str | None = None, age: int | None = None):
        self.__name = name
        self.__surname = surname
        self.__group = group
        self.__age = age

    def __str__(self):
        return f"Student {self.__name} {self.__surname} {self.__age} {self.__group}"

    @override
    def serialize_to_string(self) -> str:
        return f"{self.__name}, {self.__surname}, {self.__age}, {self.__group}"

    @override
    def deserialize(self, text: list[str]) -> None:
        self.__name = text[0]
        self.__surname = text[1]
        self.__group = text[3]
        self.__age = text[2]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if (len(name) == ''):
            raise AttributeError('name can\'t be empty')
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        if (len(surname) == ''):
            raise AttributeError('surname can\'t be empty')
        self.__surname = surname

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        if (len(group) == ''):
            raise AttributeError('group can\'t be empty')
        self.__group = group

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        if (age < 0):
            raise AttributeError('Age can\'t be negative')
        self.__age = age
