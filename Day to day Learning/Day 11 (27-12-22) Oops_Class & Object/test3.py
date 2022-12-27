class person:
    def __init__(vijay, name, surname, emailid, year_of_birth):
        vijay.name1 = name
        vijay.surname1 = surname
        vijay.emailid1 = emailid
        vijay.year_of_birth1 = year_of_birth

    def __init__(vijay, name, surname):
        vijay.name1 = name                      # IF multiple CONSTRUCTORS are given
        vijay.surname1 = surname                # like of init it will take the data of the latest
                                                # CONSTRUCTOR i.e., latest init
        
    def age(vijay, current_year):
        return current_year


anuj_var = person("anuj", "bhandari")
vijay_var = person("vijay", "rusum")
ganesh_var = person("ganesh", "paila")

print(anuj_var.age(2022))