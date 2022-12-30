"""INHERITANCE CONCEPT"""


class Car:                                          ## Parent Class

    def __init__(self, body, engine, tyre):
        self.body = body
        self.engine = engine
        self.tyre = tyre


    def milage(self):
        print("milage of this car")


class Tata(Car):                                  ## Child Class
    pass


c = Car("solid", "v6", "radial")
print(c)

t = Tata("solid1", "v8", "radial1")
print(t)
print(t.milage())
