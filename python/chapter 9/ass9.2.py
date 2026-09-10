# Bank Account
# add debit/credit logs and private balance

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        self.logs = []

    def credit(self, amount):
        self.__balance += amount
        self.logs.append(f"Credited {amount}")
        return self.__balance

    def debit(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.logs.append(f"Debited {amount}")
        else:
            self.logs.append("Debit failed: Insufficient funds")
        return self.__balance

    def get_balance(self):
        return self.__balance

    def get_logs(self):
        return self.logs

# Example
acc1 = BankAccount("David", 1000)
acc1.credit(500)
acc1.debit(300)
print(acc1.get_balance())  # Output: 1200
print(acc1.get_logs())     # Output: ['Credited 500', 'Debited 300']
