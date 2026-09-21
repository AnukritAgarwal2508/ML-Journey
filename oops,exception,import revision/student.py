

from people import SchoolMember  , Person
from exceptions import InvalidBonusError , InvalidMarksError

class Student(SchoolMember, Person):
    def __init__(self, name, marks) -> None:
        super().__init__(name)
        self.marks = marks

    def __str__(self) -> str:
        return f'{self.name} , {self.marks}'

    def __repr__(self) -> str:
        return f'Student({self.name} , {self.marks})'

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, marks):
        if marks < 0 or marks > 100:
            raise InvalidMarksError(marks)
        else:
            self.__marks = marks

    def grade(self):
        if self.marks >= 85:
            return 'A'
        if self.marks >= 60:
            return 'B'
        if self.marks >= 40:
            return 'C'
        return 'F'

    def add_bonus(self, bonus):
        if self.marks + bonus > 100 or bonus < 0:
            raise InvalidBonusError(bonus)
        self.marks = self.marks + bonus

    def is_pass(self):
        return self.marks >= 40

    def describe(self):
        super().describe()
        print(f'scored {self.marks} marks')

    def role(self):
        return 'Student'

    def __add__(self, other):
        return self.marks + other.marks

    def __lt__(self, other):
        return self.marks < other.marks


class Teacher(SchoolMember, Person):
    def role(self):
        return 'Teacher'


class LibraryMember:
    def borrow(self, book):
        print(f"{self.name} borrowed {book}")


class GradStudent(Student, LibraryMember):
    def __init__(self, name, marks, thesis_topic) -> None:
        super().__init__(name, marks)
        self.thesis_topic = thesis_topic

    def __str__(self) -> str:
        return f'{self.name} , {self.marks} , {self.thesis_topic}'

    def __repr__(self) -> str:
        return f'GradStudent({self.name} , {self.marks} , {self.thesis_topic})'

    def describe(self):
        super().describe()
        print(f'researching {self.thesis_topic}')
