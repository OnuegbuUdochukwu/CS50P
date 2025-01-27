class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n
    
    def withdraw(self, n):
        self._balance -= n



def main():
    account = Account()
    print(f"Initial balance: ${account.balance}")

    account.deposit(1000)
    print(f"After depositing $1000, balance: ${account.balance}")

    account.withdraw(500)
    print(f"After withdrawing $500, balance: ${account.balance}")



if __name__ == "__main__":
    main()