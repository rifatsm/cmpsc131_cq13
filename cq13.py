# class - design

class SavingsAccount:
    # constructor func
    def __init__(self, account_id: int, 
                 balance: float,
                 previous_balance: float,
                 annual_interest_rate: float):
        self.account_id = account_id
        self.balance = balance
        self.previous_balance = previous_balance
        self.annual_interest_rate = annual_interest_rate

    # setters - func
    def set_interest_rate(self, updated_interest_rate):
        self.annual_interest_rate = updated_interest_rate

    # getters 
    def get_monthly_interest_rate(self):
        return self.annual_interest_rate / 12 / 100

    def get_monthly_interest(self):
        return self.balance * self.get_monthly_interest_rate()

    def get_balance_change_percent(self):
        return ((self.balance - self.previous_balance) / self.previous_balance ) * 100

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.previous_balance = self.balance
            self.balance = self.balance - amount

    def deposite(self, amount: float) -> None:
            self.previous_balance = self.balance
            self.balance = self.balance + amount

# entry func
def cq() -> None:
    """
    Attributes:
    account_id (int): identifies the account.
    balance (float): the current account balance.
    previous_balance (float): the account balance at the start of the previous statement period.
    annual_interest_rate (float): the current annual interest rate, stored as a percent (e.g. 4.5 means 4.5%).
    """
    annual_interest_rate = 4.5

    account = SavingsAccount(1122, 20_000.0, 18_500.0, annual_interest_rate) # constructor
    account_2 = SavingsAccount(1123, 200_000.0, 180_500.0, annual_interest_rate) # constructor

    annual_interest_rate = 3.5

    account.set_interest_rate(annual_interest_rate)

    account.withdraw(2_500.0)
    account.deposite(3_000.0)

    """
    Prints the account id, current balance, monthly interest rate, monthly interest, and the percentage change from the previous balance to the current balance.
    """
    print(f"Account id: {account.account_id}")
    print(f"current balance: {account.balance}")
    print(f"monthly interest rate: {account.get_monthly_interest_rate() * 100:.2f}%")
    print(f"monthly interest: {account.get_monthly_interest():.2f}")
    print(f"percentage change: {account.get_balance_change_percent():.2f}%")


# name invokes the executable 
if __name__ == "__main__":
    cq()