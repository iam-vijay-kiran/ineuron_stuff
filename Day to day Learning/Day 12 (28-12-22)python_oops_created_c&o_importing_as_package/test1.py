# from test2 import person
from utils.util1 import person2

obj3 = person2("sudhanshu", "kumar", 345345)
print(obj3.yob1)

class person1:
    def __init__(self, name, surname, yob):
        self._name1 = name                  ## protected varible  _name1
        self.__surname1 = surname           ## private variable   __ surname1
        self.yob1 = yob

sudh = person1("sudhanshu", "kumar", 1990)
print(sudh._name1)
print(sudh._person1__surname1)         ## private var should be called by appending with
                                      ## _classname__var

