from pets import Pets

class Dog(Pets):
    def __init__(self, name, country, age):
        super().__init__(name,country)
        self.age = age
