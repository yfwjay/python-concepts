# We can best impliment encapsulation using a bank account class where we make balance a private attribute

# create a BankAccount Class

class BankAccount:
    def __init__(self , balance):
        self.balance = balance

    # Create a deposit method

    def deposit(self , amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Deposited =  $ {amount}")
        else:
            print("Enter a Positive Number!!")

    # create a withdraw method
    def withdraw(self , amount):
        if 0 < amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Withdrew = $ {amount}")
        else:
            print("Insufficient funds or Enter a Valid amount!")

    # Craete a get balance method
    def getbalance(self):
        return self.balance
    

# instantiate an object bank account 1

bank_account_1 = BankAccount(3000)

# call the deposit method

bank_account_1.deposit(500)

# call the withdraw method
bank_account_1.withdraw(200)

# call the get balance method
print(f"Your current balance = {bank_account_1.getbalance()}")