from csv_utility import CsvManager
from formatters import FormatterIterator, NameSurnameFormatter, WelcomeWithNameFormatter
from generators import StudentGenerator
from entities import Student

studentDatabase = CsvManager[Student]("students.csv", StudentGenerator())
studentDatabase.clear()

students = [
    Student(name="Jhon", surname="Wick", age=40, group="IA-21"),
    Student(name="Harry", surname="Poter", age=25, group="IA-22"),
    Student(name="Arnold", surname="Swarzenegger", age=50, group="IA-23"),
    Student(name="Jimi", surname="Neitron", age=20, group="IA-24")
]

studentDatabase.add(
    Student(name="John", surname="Wick", age=40, group="IA-21"))
studentDatabase.add(
    Student(name="Harry", surname="Potter", age=25, group="IA-22"))
studentDatabase.addAll(students)

print("==== DISPLAY ALL STUDENTS ====")
studentsFromDb = studentDatabase.getAll()
for student in FormatterIterator[Student](studentsFromDb):
    print(student)

print("\n==== DISPLAY STUDENTS BY FILTER ====")
filteredStudents = studentDatabase.filter(
    lambda student: student.group == 'IA-21')
for student in FormatterIterator[Student](filteredStudents, WelcomeWithNameFormatter()):
    print(student)

print("\n==== DISPLAY STUDENT BY INDEX ====")
secondStudent = studentDatabase.find_by_index(1)
print(NameSurnameFormatter().format(secondStudent))
