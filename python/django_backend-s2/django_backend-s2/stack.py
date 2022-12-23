from dataclasses import dataclass

#push, pop, top, bottom, is_empty

@dataclass
class Stack:

    __elements = []

    def get_elements(self):
        return self.__elements

    def push(self, element):
        self.__elements.append(element)
    
    def pop(self):
        return self.__elements.pop()
    
    def top(self):
        return self.__elements[-1]
    
    def bottom(self):
        return self.__elements[0]
    
    def is_empty(self):
        return len(self.__elements) == 0

stack = Stack()
print(stack.is_empty()) #True

print(stack.push(1)) #None
print(stack.push(3)) #None
print(stack.pop())   #3
print(stack.pop())   #1
print(stack.push(2)) #None
print(stack.top())   #2
print(stack.push(1)) #None
print(stack.push(4)) #None
print(len(stack.get_elements())) #3
print(stack.get_elements()) #[2, 1, 4]
print(stack.bottom()) #2
print(stack.is_empty()) #False
