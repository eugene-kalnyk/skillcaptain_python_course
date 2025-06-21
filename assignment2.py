class Person:
    def __init__ (self, name: str, age:int):
        self.name = name
        self.age = age

alice = Person("Alice", 25)
bob = Person("Bob", 30)

print (f" Name: {alice.name}. Age: {alice.age}") 
print (f" Name: {bob.name}. Age: {bob.age}")