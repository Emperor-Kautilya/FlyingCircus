class Account:
    __accno=1234
    name=""
    acc_type=""
    balance=0.0
    def Initial(self):
        self.accno=int(input("Enter account number : "))
        self.name=(input("Enter holders name : "))
        self.acc_type=(input("Enter account type : "))
        self.balance=float(input("Enter inital balance : "))
    def deposit(self):
        self.balance+=float(input("Enter amount to deposit : "))
    def displayandwithdraw(self):
        print("Amount in account :",self.balance)
        self.balance-=float(input("Enter amount to Withdraw : "))
    def diaplay(self):
        print("Account Holder :",self.name)
        print("Amount in account :",self.balance)
obj=Account()
obj.Initial()        
obj.deposit()        
obj.displayandwithdraw()
obj.diaplay()        