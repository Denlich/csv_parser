from abc import ABC, abstractmethod


class CsvSerializable(ABC):
    @abstractmethod
    def serialize_to_string(self) -> str:
        pass

    @abstractmethod
    def deserialize(self) -> None:
        pass
