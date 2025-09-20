from bank import API
from train_employe import *
import pyinputplus as pyip
class Samaneh(Employee):
    def __init__(self):
        super().__init__()


class Buy_Ticket(Samaneh):
    def __init__(self):
        super().__init__()


    def buy_ticket(self):
        print(f"{self.detail}")

    def edit_detail(self):
        pass

    def show_data(self):

        while True:
            print("1.buy ticket")
            print("2.edit detail")
            print("3.exit")
            result = input()
            if result == "1":
                self.buy_ticket()
                break
            if result == "2":
                self.edit_detail()
                break
            if result == "3":
                pass
            else :
                print("Invalid input")


class Transaction(Buy_Ticket):
    def __init__(self):
        super().__init__()
        self.amount = 0

    def deposit(self, amount):

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
        while True:
            print("please enter the amount you want to deposit: \nIf you want to go back, press 0 ")
            num = check_int()
            if num == 0:
                self.buy_ticket()
                break
            else :
                card=input("Enter the card number: ")
                exp_moth =check_int()
                exo_year = check_int()
                password = check_int()
                cvv2 = check_int()
                Valid = API ()
                flag = Valid.validate(card,exp_moth,exo_year,password,cvv2)
                if flag:
                    self.amount += amount
                    again = pyip.inputYesNo(prompt=" Do you want deposit again ? (y/n) ")
                    if again == "y":
                        continue
                    if again == "n":
                        break
                    else:
                        print("Invalid input")





user = Buy_Ticket()
user.show_data()











