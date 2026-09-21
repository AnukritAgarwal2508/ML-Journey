from abc import ABC, abstractmethod


# ===== OOP Revision — Student theme (Parts 1-15) + Exception Handling =====
# Final, working version built and tested across today's session.

# ---------- Custom exception hierarchy ----------
class StudentError(Exception):
    pass


class InvalidMarksError(StudentError):
    def __init__(self, bad_value) -> None:
        self.bad_value = bad_value
        super().__init__(f"Marks must be 0-100, got {bad_value}")


class InvalidBonusError(StudentError):
    def __init__(self, bad_value) -> None:
        self.bad_value = bad_value
        super().__init__(f"Bad Bonus value: got {bad_value}")


class ClassroomFullError(StudentError):
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        super().__init__(f"Classroom is full (capacity {capacity})")


# ---------- Abstraction ----------
class SchoolMember(ABC):
    @abstractmethod
    def role(self):
        pass


# ---------- Base class ----------
class Person:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f'{self.name}'

    def __repr__(self) -> str:
        return f'Person({self.name})'

    def describe(self):
        print(f'name : {self.name}')


# ---------- Inheritance + encapsulation + @property + magic methods + operator overloading ----------
class Student(SchoolMember, Person):
    def __init__(self, name, marks) -> None:
        super().__init__(name)
        self.marks = marks   # goes through the setter, including at construction time

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
        self.marks = self.marks + bonus   # goes through the setter

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


# ---------- Mixin (multiple inheritance) ----------
class LibraryMember:
    def borrow(self, book):
        print(f"{self.name} borrowed {book}")


# ---------- Multilevel inheritance ----------
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


# ---------- Composition + capacity limit via custom exception ----------
class Classroom:
    def __init__(self, capacity=2) -> None:
        self.students = []          # Classroom HAS a list of Students
        self.capacity = capacity

    def add(self, student):
        if len(self.students) >= self.capacity:
            raise ClassroomFullError(self.capacity)
        self.students.append(student)

    def average_marks(self):
        total = sum(s.marks for s in self.students)
        return total / len(self.students)   # true average, not floor division


if __name__ == "__main__":
    # ----- OOP recap -----
    try:
        m = SchoolMember()
    except TypeError as e:
        print("Error:", e)

    s1 = Student("Aditya", 78)
    s2 = Student("Anukrit", 92)
    print(s1 + s2)
    print(s1 < s2)
    print(s1.role(), Teacher("Ms. Rao").role())

    g = GradStudent("Anukrit", 92, "ML for Psychology")
    g.borrow("Dune")
    print(GradStudent.__mro__)
    g.describe()

    print("---")

    # ----- Exception handling: custom hierarchy + informative messages -----
    s = Student("Anukrit", 50)
    s.add_bonus(10)
    print(s.marks)                       # 60

    try:
        s.add_bonus(60)
    except InvalidBonusError as e:
        print("Error:", e)

    try:
        s.add_bonus(-200)
    except InvalidBonusError as e:
        print("Error:", e)

    print("---")

    # ----- Composition + capacity limit + finally -----
    room = Classroom(capacity=2)
    students = [Student("A", 50), Student("B", 60), Student("C", 70)]

    for stu in students:
        try:
            room.add(stu)
            print(f"{stu.name} added")
        except ClassroomFullError as e:
            print("Error:", e)
        finally:
            print(f"Attempted to add {stu.name}")

    print(room.average_marks())
