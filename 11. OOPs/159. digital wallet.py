class DigitalWallet:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance
        print(f"Wallet created for {self.owner}. Balance: Rs {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Rs {amount}. New Balance: Rs {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew Rs {amount}. Remaining: Rs {self.balance}")
        else:
            print(f"Transaction failed! Not enough money for Rs {amount}.")

    def check_balance(self):
        print(f"Current Balance for {self.owner} is Rs {self.balance}")

ali_wallet = DigitalWallet("Ali", 1000)

ali_wallet.deposit(500)      
ali_wallet.withdraw(200)      
ali_wallet.withdraw(2000)    
ali_wallet.check_balance()