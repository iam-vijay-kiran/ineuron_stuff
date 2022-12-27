class person:
    def __init__(self, name, surname, emailid, year_of_birth):
        self.name1 = name                   ## here the def __init__(self) elements points to self.name1
        self.surname1 = surname             ## these self.name1 are objects which are understood by class person
        self.emailid1 = emailid
        self.year_of_birth1 = year_of_birth


anuj_var = person("anuj", "bhandari", "anuj@gmail.com", 1994)  ## this line refers to def function
vijay_var = person("vijay", "rusum", "vijay@gmail.com", 1999)
ganesh_var = person("ganesh", "paila", "ganesh@gmail.com", 1999)
print(anuj_var.name1)
print(vijay_var.name1)
print(ganesh_var.name1)
print(type(vijay_var))

