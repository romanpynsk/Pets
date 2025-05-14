from pets import class Pets
class Cat(Pets):
    def __init__(self,name,country,age):
        super().__init__(name,country)
        self.age=age



