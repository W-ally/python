from dataclasses import dataclass

class Person:

    def __init__(self, name:str, profession:str) -> None:
        
        self.name = name
        self.profession = profession
        self.skills = []
    
    def add_skill(self, skill):
        self.skills.append(skill)
    
    def __str__(self) -> str:
        return f'I am {self.name} and my profession is {self.profession}, skills: {self.skills}'

@dataclass
class Vehicle:
    
    brand:str
    year:str

    def __str__(self) -> str:
        return f'The brand of the car is {self.brand} and year is {self.year}'

# person = Person('Jorge', 'Engineer')
# print(person)
# person.add_skill('Python')
# person.add_skill('POO')
# print(person)

vehicle = Vehicle('BMW', '2017')
print(vehicle)