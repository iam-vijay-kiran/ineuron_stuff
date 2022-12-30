"""SINGLE INHERITANCE, MULTIPLE INHERITANCE, MULTI-LEVEL INHERITANCE"""

"""This is the example of MULTI-LEVEL INHERITANCE"""


class Bank:

    testing_variable = "testing"

    def transaction(self):
        print("total transaction value")
    def account_opening(self):
        print("this will show you your account opening status")
    def deposite(self):
        print("this will show your deposited amount")


class HDFC_bank(Bank):
    def hdfc_to_icici(self):
        print("this will show you all the transaction happened to icici through hdfc")


class Icici(HDFC_bank):
    pass


i = Icici()
i.hdfc_to_icici()
i.deposite()
i.account_opening()
i.transaction()

