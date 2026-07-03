class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
        
        
    def debit(self,amount):
        self.balance-=amount
        print(f"Rs.{amount} was debitted and now total balance is RS.{self.balance}")
        
    def credit(self,amount):
        self.balance+=amount
        print(f"Rs.{amount} was creditted and now total balance is RS.{self.balance}")

#objects =
A1=Account(10000,"moiz")
A1.credit(2000)
A1.debit(5000)
A2=Account(200,"ali")
A2.debit(500)
