"""This is the example for MULTIPLE INHERITANCE"""


class Bank:

    def transaction(self):
        print("total transaction value")

    def account_opening(self):
        print("this will show you your account opening status")

    def deposite(self):
        print("this will show your deposited amount")

    def test(self):
        print("this is a method from bank class")


class HDFC_bank:
    def hdfc_to_icici(self):
        print("this will show you all the transaction happened to icici through hdfc")

    def test(self):
        print("this is a method from hdfc_bank class ")


class Ineuron_bank:
    def account_status_icici(self):
        print("print an account status in icici ")


class Icici(HDFC_bank, Bank, Ineuron_bank):
    pass


"""if there is a conflict with respect to method/variable name 
 in class is same then we get method of 1st argument passed in child class"""


i = Icici()
i.hdfc_to_icici()
i.transaction()
i.deposite()
i.account_opening()
i.test()
i.account_status_icici()
