import csv
from io import FileIO
from typing import Generic, TypeVar
from pathlib import Path

T = TypeVar('T')


class CsvManager(Generic[T]):
    def __init__(self, fileName: str, generator):
        self.__file = fileName
        self.__items = generator

    @property
    def __file(self) -> FileIO:
        return self.__file

    @__file.setter
    def __file(self, fileName: str) -> None:
        self.__filePath = Path(__file__).parent.absolute() / fileName
        self.__filePath.touch(exist_ok=True)
        self.__file = FileIO(self.__filePath, mode='r')

    @property
    def __items(self) -> list[T]:
        return self.__items

    @__items.setter
    def __items(self, generator) -> None:
        with self.__file as csv_file:
            file_content = csv_file.read().decode('utf-8')

            reader = csv.reader(file_content.splitlines())
            for row in reader:
                item = generator.generate(row)
                self.__items.append(item)
