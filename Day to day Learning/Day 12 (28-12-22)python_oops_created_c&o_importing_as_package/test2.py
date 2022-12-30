import test1
print(test1)
obj3 = test1.person1("sudhanshu","kumar",1994)
print(obj3.yob1)
print(obj3._name1)
print(obj3._person1__surname1)


class person :
    _name = "sudh"                 ## protected variable
    __surname = "kumar"            ## private variable
    yob = 1990

    def _age(self, current_year):           ## protected funtion
        return current_year - self.yob

    def __age1(self, current_year ):     ## private function
        return current_year - self.yob

obj = person()
print(obj._age(2022))                ## calling protected function
print(obj._person__age1(2022))       ## calling private function



class employee(person) :          ## inheritance - child class
    _name = "sudhanshu"
    __surname = "singh"
    yob = 1991

obj1 = employee()
print(obj1._age(2022))            ##  using inheritance calling protected funtion
print(obj1._person__age1(2022))   ## private funtion is called using inheritance

print(obj1.yob)
print(obj1._name)
print(obj1._person__surname)