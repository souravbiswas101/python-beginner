class BankAccount:
    def __init__(self, balance = 0):
        self.__balance = balance

    def deposit(self, amount):
        if amount>0:
            self.__balance +=amount
            print(f"Deposited ${amount}. Current balance: ${self.__balance}")

        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount> 0 and amount<=self.__balance:
            self.__balance -= amount
            print(f"Withdraw &{amount}. Current balance: ${self.__balance}")


        else:
            print("Invalid withrawal amount or insufficient balance.")


    def get_balance(self):
        return self.__balance
    

class SavingsAccount(BankAccount):
    def account_type(self):
        print("This is a savings account.")

class CurrentAccount(BankAccount):
    def account_type(self):
        print("This is a Current Account.")



savings = SavingsAccount(500)
current = CurrentAccount(1000)

savings.account_type()
current.account_type()

savings.deposit(200)
current.withdraw(300)

print(f"Savings Account Balance: $ {savings.get_balance()}")
print(f"Current Account Balance: ${current.get_balance()}")