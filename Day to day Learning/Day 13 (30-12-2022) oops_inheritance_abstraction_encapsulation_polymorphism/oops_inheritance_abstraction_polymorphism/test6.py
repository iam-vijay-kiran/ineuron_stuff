"""    POLYMORPHISM    """


class Ineuron:
    def students(self):
        print("print the student details ")


class Class_type:
    def students(self):
        print("print the class type of students ")


def Ineuron_external(a):
    a.students()


"""same funciton 'Ineuron_external' but calls different class 
         and behaving like  common interface """

i = Ineuron()
j = Class_type()
Ineuron_external(i)
Ineuron_external(j)






# def test(a, b):
#     return a+b
#
#
# print(test(4, 5))
# print(test("vijay ", "kiran"))
