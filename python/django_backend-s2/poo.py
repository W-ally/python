from abc import ABC, abstractmethod

class Person(ABC):
    
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    @abstractmethod
    def say_hello(self):
        '''this method should be implemente by subclass'''
    
    @abstractmethod
    def say_goodbye(self):
        '''this method should be implemente by subclass'''
    
    def __str__(self) -> str:
        return f"{self.name} {self.age}"


class Student(Person):

    def __init__(self, name, age, school) -> None:
        super().__init__(name, age)
        self.school = school
        self.__is_enabled = True
    
    def say_hello(self):
        return f"Hello my name is {self.name}"
    
    def say_goodbye(self):
        return f"Bye from {self.name}"
    
    def enable(self):
        self.__is_enabled = True
    
    def disable(self):
        self.__is_enabled = False
    
    def get_status(self):
        return self.__is_enabled
    
    def __str__(self) -> str:
        return super().__str__() + f" i am student from {self.school} {self.__is_enabled}"

student = Student('Jorge', 30, 'Tecnologico Comfenalco, Cartagena')

print(student)
# print(student.__is_enabled)
print(student.get_status())
