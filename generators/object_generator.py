from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from ..csv import CsvSerializable

T = TypeVar('T', bound=CsvSerializable)


class ObjectGenerator(ABC, Generic[T]):
    @abstractmethod
    def generate(self, serialized_object: list[str]) -> T:
        pass
