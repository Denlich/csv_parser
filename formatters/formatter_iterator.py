from typing import Iterator, Generic, TypeVar, List, Optional
from . import Formatter

T = TypeVar('T')


class FormatterIterator(Iterator[str], Generic[T]):
    def __init__(self, items: List[T], formatter: Optional[Formatter[T]] = None):
        self.__items = items
        self.__formatter = formatter
        self.__index = 0

    def __iter__(self) -> 'FormatterIterator[T]':
        return self

    def __next__(self) -> str:
        if self.__index < len(self.__items):
            item = self.__items[self.__index]
            if self.__formatter != None:
                formatted_item = self.__formatter.format(item)
            else:
                formatted_item = str(item)
            self.__index += 1
            return formatted_item
        else:
            raise StopIteration

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, items: List[T]):
        self.__items = items

    @property
    def formatter(self):
        return self.__formatter

    @formatter.setter
    def formatter(self, formatter: Optional[Formatter[T]]):
        self.__formatter = formatter
