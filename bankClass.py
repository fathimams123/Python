class Bank:
    def __init__(self,accNo,name,accType,balance=0):
        self.accNo=accNo
        self.name=name
        self.accType=accType
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposit successfull! New Balance: {self.balance}")
        else:
            print("Invalid Deposit Amount.Enter Positive Value")

    def withdrew(self,amount):
        if amount>0:
            if amount<=self.balance:
                self.balance-=amount
                print(f"New Balance: {self.balance}")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Withdrew Amount")

    def display(self):
        print("\nAccount Number: ",self.accNo)
        print("\nAccount Holder Name: ",self.name)
        print("\nAccount Type: ",self.accType)
        print("\nAccount Balance",self.balance)


b1=Bank(1002,"Nidhi","Savings",0)
b1.display()
while True:
    print("\n**Menu**\n1.Deposit\n2.Withdrew\n3.Display\n4.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        d=float(input("\nEnter Amount To Be Deposit:"))
        b1.deposit(d)
    elif choice==2:
        w=float(input("\nEnter Amount To Withdrew:"))
        b1.withdrew(w)
    elif choice==3:
        b1.display()
    elif choice==4:
        print("Exit")
        break
    else:
        print("Enter Valid Choice")
