class person:
    def __init__(vijay, name, surname, emailid, year_of_birth):
        vijay.name1 = name                   ## here the def __init__(self) elements points to self.name1
        vijay.surname1 = surname             ## these self.name1 are objects which are understood by class person
        vijay.emailid1 = emailid
        vijay.year_of_birth1 = year_of_birth

    def age(vijay,current_year  ):
        return current_year - vijay.year_of_birth1


anuj_var = person("anuj", "bhandari", "anuj@gmail.com", 1994)  ## this line refers to def function
vijay_var = person("vijay ", "rusum", "vijay@gmail.com", 1999)
ganesh_var = person("ganesh", "paila", "ganesh@gmail.com", 1999)
print(vijay_var.name1 + vijay_var.surname1)
print(anuj_var.name1)
print(vijay_var.name1)
print(ganesh_var.name1)
print(type(vijay_var))

v = "vijay "
s = "rusum "
print(v+s)

print(vijay_var.age(2022))
