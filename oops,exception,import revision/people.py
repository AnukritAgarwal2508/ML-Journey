from abc import ABC, abstractmethod

class SchoolMember(ABC):
    @abstractmethod
    def role(self):
        pass


class Person:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f'{self.name}'

    def __repr__(self) -> str:
        return f'Person({self.name})'

    def describe(self):
        print(f'name : {self.name}')
