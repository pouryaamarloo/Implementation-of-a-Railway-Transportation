from train_employe import *
class Buy_Ticket():
    def __init__(self):
        super().__init__()


    def buy_ticket(self):
        pass

    def edit_detail(self):
        pass

class Transaction(Buy_Ticket):
    def __init__(self):
        super().__init__()

    def deposit(self):

        def check_int():
            while True:
                try:
                    amount = int(input())
                except ValueError:
                    print("Please enter a number.")
                if amount < 0:
                    print("Please enter a positive number.")
                else:
                    return amount
        print("please enter the amount you want to deposit: \nIf you want to go back, press 0 ")
        amount = check_int()
        if amount == 0:
            self.buy_ticket()
        else :
            card=input("Enter the card number: ")
            exp_moth =check_int()





