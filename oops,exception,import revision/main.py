from student import Student , Teacher , LibraryMember , GradStudent
from classroom import Classroom
from exceptions import ClassroomFullError

s1 = Student("Aditya", 78)
s2 = Student("Anukrit", 92)
print(s1 + s2)

room = Classroom(capacity=2)
room.add(s1)
room.add(s2)
try:
    room.add(Student("C", 70))
except ClassroomFullError as e:
    print("Error:", e)
print(room.average_marks())