import random

class Account:
    def __init__(self, acc_number, name, password, balance=0):
        self.acc_number = acc_number
        self.name = name
        self.__password = password
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive!")
            return
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount, password):
        if password != self.__password:
            print("Incorrect password!")
            return
        if amount > self.__balance:
            print("Insufficient funds!")
            return
        self.__balance -= amount
        print(f"Withdrawn {amount}. New balance: {self.__balance}")

    def check_balance(self, password):
        if password != self.__password:
            print("Incorrect password!")
            return
        print(f"Balance: {self.__balance}")

    def transfer(self, target_account, amount, password):
        if password != self.__password:
            print("Incorrect password!")
            return
        if amount > self.__balance:
            print("Insufficient funds!")
            return
        self.__balance -= amount
        target_account.__balance += amount
        print(f"Transferred {amount} to {target_account.name}. New balance: {self.__balance}")


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        name = input("Enter your name: ").strip().title()
        password = input("Enter your password: ")
        try:
            deposit = float(input("Enter initial deposit: "))
            if deposit < 0:
                print("Deposit cannot be negative!")
                return
        except ValueError:
            print("Invalid amount!")
            return

        acc_number = random.randint(100000, 999999)
        account = Account(acc_number, name, password, deposit)
        self.accounts.append(account)
        print(f"Account created! Your account number is {acc_number}")

    def find_account_by_number(self, acc_number):
        for acc in self.accounts:
            if acc.acc_number == acc_number:
                return acc
        return None

    def find_accounts_by_name(self, name):
        return [acc for acc in self.accounts if acc.name.lower() == name.lower()]

    def menu(self):
        while True:
            print("\n1. Create Account\n2. Find Account\n3. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.create_account()
            elif choice == "2":
                sub = input("Search by (1) Name or (2) Account Number? ")
                if sub == "1":
                    name = input("Enter name: ")
                    results = self.find_accounts_by_name(name)
                    if not results:
                        print("No accounts found.")
                        continue
                    for acc in results:
                        print(f"Account Number: {acc.acc_number}, Name: {acc.name}")
                    acc_num = int(input("Enter account number to access: "))
                    acc = self.find_account_by_number(acc_num)
                    if acc:
                        self.account_actions(acc)
                    else:
                        print("Account not found.")
                elif sub == "2":
                    acc_num = int(input("Enter account number: "))
                    acc = self.find_account_by_number(acc_num)
                    if acc:
                        self.account_actions(acc)
                    else:
                        print("Account not found.")
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")

    def account_actions(self, acc):
        while True:
            print(f"\nAccount: {acc.name} ({acc.acc_number})")
            print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Transfer\n5. Back to Main Menu")
            action = input("Choose action: ")
            if action == "1":
                amount = float(input("Enter amount to deposit: "))
                acc.deposit(amount)
            elif action == "2":
                amount = float(input("Enter amount to withdraw: "))
                password = input("Enter password: ")
                acc.withdraw(amount, password)
            elif action == "3":
                password = input("Enter password: ")
                acc.check_balance(password)
            elif action == "4":
                target_acc_num = int(input("Enter target account number: "))
                target_acc = self.find_account_by_number(target_acc_num)
                if not target_acc:
                    print("Target account not found.")
                    continue
                amount = float(input("Enter amount to transfer: "))
                password = input("Enter your password: ")
                acc.transfer(target_acc, amount, password)
            elif action == "5":
                break
            else:
                print("Invalid option!")


# Run the program
bank = Bank()
bank.menu()
