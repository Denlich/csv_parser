from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class Formatter(ABC, Generic[T]):
    @abstractmethod
    def format(self, item: T) -> str:
        pass
