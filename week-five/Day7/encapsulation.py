class BankAccount:
    def __init__(self , balance):
        self.__balance = balance 
    
    # Deposit method
    def deposit(self , amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited =  $ {amount}")
        else:
            print("Enter a Positive Number!!")
    def withdraw(self , amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew = $ {amount}")
        else:
            print("Insufficient funds or Enter a Valid amount!")
    def getbalance(self):
        return self.__balance


# object

account = BankAccount(2000)

account.deposit(250)

account.withdraw(100)

print(f"Your current balance = {account.getbalance()}")