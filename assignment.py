class Account:
    def __init__(self,name,account_number):
        self.balance=0
        self.name=name
        self.account_number=account_number
        self.deposits = []
        self.withdrawals =[]
        self.transctions=100
        
        
    def deposit(self,amount):
        if amount<=0:
            return f"Deposit amount should be more than zero"
        else:
            self.balance += amount
            self.deposits.append(f"You have deposited{amount}")
            return f"You have deposited {amount}. Your new balance is {self.balance}. {self.deposits}"  

    def withdraw(self,amount):
        if amount>self.balance:
             return f"Your balance is {self.balance}, you cannot withdraw the {amount}" 
        elif amount<=0:
            return f"Amount must be greater than zero" 
        else:
            self.balance-=amount+self.transctions
            self.withdrawals.append(f"you have withdraw{amount}")
            return f"you have withdraw {amount} your balance is {self.balance}. {self.withdrawals}" 
    
def deposits_statement(self):
        for statements in self.deposits:
            print(statements)
def withdraws_statement(self):
        for staments in self.withdraws:
            print(staments)
def current_balance(self):
        balance = self.balance
        print(balance)

