class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough money in the account.")
        
try:
    withdraw(50, 100)
except InsufficientFundsError as e:
    print(e)