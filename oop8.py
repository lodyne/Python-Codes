#BANK MANAGEMENT SYSTEM
class Bank:
    #initial_amount=10000
    def __init__(self,balance):
        self.balance=0

class Account(Bank):
    #def __init__(self,balance):
        #super().__init__(balance)
    
    def deposit(self):
        print("Enter amount to deposit")
        initial_amount=int(input())
        #self.balance=int(self.balance + self.initial_amount)
        self.balance+=initial_amount
        print("The deposit amount is: ",initial_amount)
    
    def withdraw(self):
        print("Enter amount to withdraw")
        initial_amount=int(input())
        if self.balance >= initial_amount:
            self.balance-=initial_amount
            print("The withdraw amount is: ",initial_amount)
        else:
            print("Invalid")
            
    
    def current_balance(self):
        print ("The current balance is: ",self.balance)

class Customer(Account):
    def createAccount(self):
        self.accNo= int(input("Enter the account no : "))
        self.name = input("Enter the account holder name : ")
        self.type = input("Enter the type of account [C/S] : ")
        #self.balance = int(input("Enter The initialial amount(>=500 for Saving and >=1000 for current",self.balance))
        print("\n\n\nAccount Created")
    
    def showAccount(self):
        print("Account Number : ",self.accNo)
        print("Account Holder Name : ", self.name)
        print("Type of Account",self.type)
        #print("Balance : ",self.balance)
    
    def modifyAccount(self):
        print("Account Number : ",self.accNo)
        self.name = input("Modify Account Holder Name :")
        self.type = input("Modify type of Account :")
        self.deposit = int(input("Modify Balance :"))
    
class BankInfo:
    def login(self):
        print("WELCOME,PLEASE LOGIN")
        self.name=input("Enter your username: ")
        self.password=input("Enter your password: ")

    def menu(self):
        print("1.NEW ACCOUNT")
        print("2.DEPOSIT")
        print("3.WITHDRAW")
        print("4.BALANCE ENQUIRY")
        print("5.MODIFY ACCOUNT")
        print("6.EXIT")
        print("Select your option (1-6) ")
        print(" ")
        print()

class Main:
    #object=Account("")
    object=Customer('')
    #print(object.balance)

    object.createAccount()
    object.showAccount()
    object.deposit()
    #print(object.balance)

    object.withdraw()
    #print(object.balance)
    
    object.current_balance()

