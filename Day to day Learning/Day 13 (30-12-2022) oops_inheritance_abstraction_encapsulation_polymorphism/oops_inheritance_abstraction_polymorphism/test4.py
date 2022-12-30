"""      DATA ABSTRACTION - hiding data behind something like class etc     """

class Ineuron:
    # private variable
    __student = "data science"
    achievers = "achieved"

    def students(self):
        print("print the class of students", Ineuron.__student)


""" Here we are hiding student variable as protected mode. So can only
    be accessed by entering to class and then to variable   """

i = Ineuron()
i.students()

''' Abstraction data '''
print(i._Ineuron__student)

'''not abstracted data'''
print(i.achievers)