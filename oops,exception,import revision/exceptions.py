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
