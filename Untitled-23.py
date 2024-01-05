class Person:
    

    def __init__(self, name, age):
        
        self.name = name
        self.age = age

    def greet(self):
        
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


person1 = Person("durgarao", 24)
person2 = Person("raju", 25)

person1.greet()  
person2.greet()  
