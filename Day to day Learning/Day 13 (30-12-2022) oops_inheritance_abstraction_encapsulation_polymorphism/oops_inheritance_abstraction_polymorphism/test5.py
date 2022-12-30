"""  ENCAPSULATION - now allowing to modify hidden data behind something like class etc """


class Ineuron:
    def __init__(self):
        self.students1 = "data science"

    def students(self):
        print(self.students1)


i = Ineuron()
i.students()
i.students1 = "data analytics"    """ with help of object private variable can be changed """
i.students()


class Ineuron1:
    def __init__(self):
        self.__students1 = "data science"

    def students(self):
        print(self.__students1)

    """setter method/function to change obj variable"""

    def student_change(self, new_value):
        self.__students1 = new_value


i1 = Ineuron1()
i1.students()
i1.__students1 = " big data "      """ with help of object private variable cannot be changed"""
i1.students()
i1.student_change("vijay")
i1.students()
