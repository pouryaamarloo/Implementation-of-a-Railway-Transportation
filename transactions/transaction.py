from bank import API
from train_employe import *
import pyinputplus as pyip
class Normal_User_Panel(Employee):
    def __init__(self):
        super().__init__()


class Buy_Ticket(Normal_User_Panel):
    def __init__(self):
        super().__init__()
        self.wallet = 0


    def buy_ticket(self):

        def check_int():
            while True:
                try:
                    choice = int(input(""))
                except ValueError:
                    print("Please enter a number.")
                    continue
                if choice :
                    return choice
        if not self.detail :
            print("You don't have any tickets to buy.")
            self.show_data()
            return
        for i in self.detail:
            print(f"train name = {i['train_name']} : train_id = {i['id']},\nline name {i['line_name']},\n price : {i['price']}  amount : {i['amount']} ")
        print("please enter train id ")
        choice = check_int()
        print("Please enter the number of tickets you want.")
        Count = check_int()
        print(f"The amount of money in your wallet is: {self.wallet}")
        for i in self.detail:
            if choice == i['id']:
                price = i['price']
            else:
                print("The ID you’re looking for was not found.")

        price = price * Count
        if price > self.wallet:
            print("You don't have enough money.")
            again = pyip.inputYesNo(prompt=" Do you want to increase your wallet balance? (y/n) ")
            if again == "n":
                self.show_data()
                return
            else :
                user = Transaction()
                print("Please enter the amount of money you want to deposit into your wallet.")
                depos = check_int()
                user.deposit(depos)
                self.buy_ticket()
                return

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











