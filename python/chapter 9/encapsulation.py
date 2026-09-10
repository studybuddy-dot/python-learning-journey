#encapsulation example

class Account:
    def __init__(self,bal):
        self.__balance=bal     #private 

    def show__balance(self):
        print("Balance:",self.__balance)