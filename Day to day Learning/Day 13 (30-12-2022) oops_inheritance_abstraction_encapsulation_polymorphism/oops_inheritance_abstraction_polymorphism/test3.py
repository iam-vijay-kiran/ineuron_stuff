class Ineuron:
    def student(self):
        print("print the details of all the students")

    def achievers(self):
        print("print the list of all the achiever")

    def hall_of_fame(self):
        print("print everyone from hall of fame")


class Ineuron_vision(Ineuron):

    def student(self):                                  ## method overiding
        print("these are the filter students list ")


iv = Ineuron_vision()
iv.student()