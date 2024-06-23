from typing import override
from . import Formatter
from ..entities import Student


class NameSurnameFormatter(Formatter[Student]):
    @override
    def format(self, item: Student) -> str:
        return f"{item.name} {item.surname}"
