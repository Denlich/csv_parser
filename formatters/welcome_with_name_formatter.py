from typing import override
from formatters import Formatter
from entities import Student


class WelcomeWithNameFormatter(Formatter[Student]):
    @override
    def format(self, item: Student) -> str:
        return f"Hello, I am {item.name}"
