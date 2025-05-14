from pets import class Pets
class Cat(Pets):
    def __init__(self,name,color,age):
        super().__init__(name,color)
        self.age=age



