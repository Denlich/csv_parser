import csv
from pathlib import Path
from io import FileIO
from typing import List, TypeVar, Generic, Callable, Any

from csv_utility import CsvSerializable
from generators import ObjectGenerator

T = TypeVar('T', bound=CsvSerializable)


class CsvManager(Generic[T]):
    __items: list[T] = list()
    __filePath: Path = ""

    def __init__(self, fileName: str, generator: ObjectGenerator[T]):
        self.file = fileName
        self.items = generator

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, fileName: str):
        self.__filePath = Path(
            __file__).parent.absolute().parent.absolute() / fileName
        self.__filePath.touch(exist_ok=True)
        self.__file = FileIO(self.__filePath, mode='r')

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, generator):
        with self.__file as csv_file:
            file_content = csv_file.read().decode('utf-8')

            reader = csv.reader(file_content.splitlines())
            for row in reader:
                item = generator.generate(row)
                self.__items.append(item)

    def getAll(self) -> list[T]:
        return self.__items

    def find_by_index(self, index: int) -> T:
        return self.items[index]

    def filter(self, filter_predicate: Callable[[T], Any]) -> List[T]:
        return list(filter(filter_predicate, self.__items))

    def __addInternal(self, item: T) -> None:
        self.__items.append(item)
        with open(self.__filePath, mode="a") as file:
            file.write(item.serialize_to_string() + "\n")

    def add(self, item: T) -> None:
        self.__addInternal(item)

    def clear(self) -> None:
        self.__items = []
        with open(self.__filePath, 'w'):
            pass

    def addAll(self, list: list[T]):
        for item in list:
            self.add(item)
