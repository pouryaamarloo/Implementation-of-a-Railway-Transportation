from bank import API
from train_employe import *
import pyinputplus as pyip
from buy_ticket import *


class Transaction(Buy_Ticket):
    def __init__(self):
        super().__init__()

    def deposit(self, amount):

        def check_int():
            while True:
                try:
                    a = int(input())
                except ValueError:
                    print("Please enter a number.")
                    continue
                if a < 0:
                    print("Please enter a positive number.")
                else:
                    return a
        while True:
            print("please enter the amount you want to deposit: \nIf you want to go back, press 0 ")
            num = check_int()
            if num == 0:
                self.buy_ticket()
                break
            else :
                card=input("Enter the card number: ")
                exp_moth =check_int()
                exp_year = check_int()
                password = check_int()
                cvv2 = check_int()
                Valid = API ()
                flag = Valid.pay(card,exp_moth,exp_year,password,cvv2,num)
                if flag:
                    self.amount += num
                    again = pyip.inputYesNo(prompt=" Do you want deposit again ? (y/n) ")
                    if again == "y":
                        continue
                    else:
                        break
        return


user = Buy_Ticket()
user.show_data()











