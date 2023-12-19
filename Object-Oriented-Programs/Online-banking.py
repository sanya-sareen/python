class Customer:
    '''
    This class basically handles operations for customers
    '''
    bank_name = "YOLO-Bank"
    def __init__(self,cust_name, balance = 0.0):
        self.cust_name = cust_name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Balance after deposit:", self.balance)

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient funds..operations cannot be performed")
        else:
            self.balance = self.balance - amount
            print("After withdraw, balance is:", self.balance)

print("Welcome to:-",Customer.bank_name)

name = input("Enter your name:")
c= Customer(name)

while True:
    print("D:Deposit\n W:Withdraw \n E: Exit")
    option = input("Choose your options:-")

    if option.lower() == 'd':
        amount = float(input("Enter amount to deposit:"))
        c.deposit(amount)

    elif option.lower() == 'w':
        amount = float(input("Enter the amount to withdraw:"))
        c.withdrawal(amount)

    elif option.lower() == 'e':
        print("Thanks for Banking")
        break

    else:
        print("your option is invalid...Please choose valid option")
