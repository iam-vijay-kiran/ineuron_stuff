class person2:
    def __init__(self, name, surname, yob):
        self._name1 = name                  ## protected varible  _name1
        self.__surname1 = surname           ## private variable   __ surname1
        self.yob1 = yob

sudh = person2("sudhanshu","kumar",1990)
print(sudh._name1)
print(sudh._person2__surname1)