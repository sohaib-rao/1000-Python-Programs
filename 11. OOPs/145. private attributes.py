class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # Private attribute

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
# print(account.__balance) # This would cause error
print(account.get_balance()) 