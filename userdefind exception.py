class FundsError(Exception):
    pass
def without(balance,amount):
    if amount>balance:
        raise Funds("withdrawl amount exceeds available balance.")
    return balance-amount
try:
    amount_balance = 350

finally:   
    account_balance=withdraw(account_balance,150)
    print(account_balance)
except Funds as e:
    print(f"Error:(e)")
