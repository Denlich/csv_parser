from typing import override
from . import ObjectGenerator
from entities import Student


class StudentGenerator(ObjectGenerator[Student]):
    @override
    def generate(self, serialized_object: list[str]) -> Student:
        new_student = Student()
        new_student.deserialize(serialized_object)
        return new_student
