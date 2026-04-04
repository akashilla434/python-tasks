class bankaccount:
    def __init__(self,acc_no,balance):
            self.accont_no= acc_no
            self.balance=balance
    def deposit(self,amount):
            self.balance+= amount
            print("amount deposited:",amount)
    def withdraw(self,amount):
            if amount <= self.balance:
                self.balance-= amount
                print("amount withdraw:",amount)
            else:
                print("insuffcient balance")
    def display(self):
            print("account number:",self.acc_no)
            print("balance:",self.balance)
b1=bankaccount(12345,1000)

b1.deposit(500)
b1.withdraw(300)
b1.display()
                  
