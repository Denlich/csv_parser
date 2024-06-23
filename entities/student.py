from ..csv import CsvSerializable
from typing import override


class Student(CsvSerializable):
    def __init__(self, name: str, surname: str, age: int, group: str):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__group = group

    @property
    def __name(self) -> str:
        return self.__name

    @__name.setter
    def __name(self, value) -> None:
        self.__name = value

    @property
    def __surname(self) -> str:
        return self.__surname

    @__surname.setter
    def __surname(self, surname: str) -> None:
        self.__surname = surname

    @property
    def __age(self) -> int:
        return self.__age

    @__age.setter
    def __age(self, age: int) -> None:
        self.age = age

    @property
    def __group(self) -> str:
        return self.__group

    @__group.setter
    def __group(self, group: str) -> None:
        self.__group = group

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
