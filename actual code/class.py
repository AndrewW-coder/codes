class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self):
        print("Hello my name is " + self.name)

Joe = Person("Joe", 23)

print(Joe.age)