# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

# Solve:

class Bank:
    bank_name = "HBL"

    def __init__ (self, account_holder):
        self.account_holder = account_holder


    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank Name: {self.bank_name}")       


account1 = Bank("Zoha")
account2 = Bank("Abrish")

account1.display()
account2.display()


Bank.change_bank_name("UBL")


account1.display()
account2.display()


