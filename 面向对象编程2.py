class BankAccount:
    interest_rate = 0.03

    def __init__(self, name, money):
        self.name = name
        self.money = money

    def deposit(self, amount):
        print(f'{self.name} deposits {amount}.')
        self.money = self.money + amount

    def withdraw(self, amount):
        print(f'{self.name} withdraws {amount}.')
        self.money = self.money - amount

    def showinfo(self):
        print(f'Owner: {self.name}\nBalance: {self.money}')
        

    def set_interest_rate(new_rate):
        BankAccount.interest_rate = new_rate

    def is_valid_amount(amount):
            if amount <= 0 :
                print("Wrong number!")

Owner1 = BankAccount('Lily', 10000)
Owner2 = BankAccount('Mike', 20000)        

Owner1.showinfo()

Owner2.deposit(20000)
Owner2.showinfo()

BankAccount.set_interest_rate(0.05)
print(Owner1.interest_rate)


BankAccount.is_valid_amount(0)