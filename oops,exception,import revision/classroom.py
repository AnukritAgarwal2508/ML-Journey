
from exceptions import ClassroomFullError

class Classroom:
    def __init__(self, capacity=2) -> None:
        self.students = []
        self.capacity = capacity

    def add(self, student):
        if len(self.students) >= self.capacity:
            raise ClassroomFullError(self.capacity)
        self.students.append(student)

    def average_marks(self):
        total = sum(s.marks for s in self.students)
        return total / len(self.students)
