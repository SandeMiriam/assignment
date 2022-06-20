from datetime import datetime


class Account:
    def __init__(self,account_name, account_number):
        self.balance=0
        self.account_name=account_name
        self.account_number=account_number
        self.deposits=[]
        self.withdrawals=[]
        self.transaction= 100
        self.date=datetime.now()
        self.loan_balance=0
        

        
    def deposit(self,amount):
        if amount <=0:
            return f"Deposit amount should be more than zero"
        else:
            self.balance += amount
            self.deposits.append({"date":self.date.strftime('%c'), "amount":amount,"narration":"deposit"})
            return f"You deposited {amount}.Your new balance is {self.balance}"
             
    
    def withdraw(self, amount):
        if (amount+self.transaction)>self.balance:
            return f"Your balance is {self.balance}, you cannot withdraw the {amount}"
        elif amount<=0:
            return f"Amount must be greater than zero"
        else:    
            self.balance-=(amount +self.transaction)
            self.withdrawals.append({"date":self.date.strftime('%c'), "amount":amount,"narration":"Withdrawn"})
            return f"You withdrew {amount} and the transaction cost was {self.transaction}.Your new balane is {self.balance}"
        
    def deposits_statement(self):
        for depo in self.deposits:
            print(depo)
        
    def withdrawals_statement(self):
        for withdraws in self.withdrawals:
            print(withdraws) 
            
    def current_balance(self):
        balance=self.balance
        print("Your current balance is {balance}")  
        
    def full_statement(self):
        statements= (*self.deposits,*self.withdrawals)    
        for statement in statements:
            print(statement)  
            
    def borrow(self,amount): 
        
        sum=0
        for depo in self.deposits:
            sum+=depo["amount"]
        if (len(self.deposits)) <10:
            print(f"Can't be lended this {amount} you've deposited less than 10 times.") 
        elif(amount <100):
            print("You can't borrow  less than 100") 
        elif amount > (sum//3):
            print("You've exceeded the loan limit")
        elif self.balance==0:
            print("You can't borrow.Your account balance is 0")    
        elif self.loan_balance>0:
            print(f"You have an outstanding loan of {self.loan_balance}.You can't borrow this {amount}")    
        else:
            self.loan_balance+=(amount+(amount*0.03))
            print(f"Your loan is {amount} and an interest of{amount*0.03} and total loan amount is {self.loan_balance}")    
            
    def loan_repayment(self,amount):
        overpayment=amount-self.loan_balance
        loan_payment=amount-overpayment
        if amount<0:
            print(f"Repayment amount has to be more than 0")
        elif amount <= self.loan_balance:
            self.loan_balance-=amount
            print(f"Your loan balance is {self.loan_balance} ")    
        else:
            self.loan_balance-=loan_payment
            self.balance+=overpayment
            print(f"You have an overpayment of {overpayment}") 
    
    def transfer(self, amount, acc2):
        if amount > self.balance:
            print("You don't have sufficient amount of money to transfer this amount.")
        elif amount<=0:
            print("Put a valid amount of money.")
        else:    
            self.balance-=amount
            acc2.balance+=amount
            print(f"{self.account_name} you've sent{amount} to {acc2.account_name}") 


