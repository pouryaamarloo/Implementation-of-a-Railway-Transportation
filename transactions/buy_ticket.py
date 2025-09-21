from bank import API
from train_employe import *
import pyinputplus as pyip
from transaction import *

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
                if choice:
                    return choice

        if not self.detail:
            print("You don't have any tickets to buy.")
            self.show_data()
            return
        for i in self.detail:
            print(
                f"train name = {i['train_name']} : train_id = {i['id']},\nline name {i['line_name']},\n price : {i['price']}  amount : {i['amount']} ")
        while True:
            print("please enter train id ")
            choice = check_int()
            print("Please enter the number of tickets you want.")
            Count = check_int()
            price = 0
            print(f"The amount of money in your wallet is: {self.wallet}")
            for i in self.detail:
                if choice == i['id']:
                    price = i['price']
                    if Count > i['amount']:
                        print(
                            "The train capacity is less than what you selected\nif you want to back last panel enter 0")
                        Count = pyip.inputInt(
                            prompt="Please enter the number of tickets you want: ",
                            min=0,
                            max=i['amount']
                        )
                        if Count == 0:
                            self.show_data()
                            return
                        else:
                            break
                    else:
                        break
            if price == 0:
                print("The ID you’re looking for was not found.")
            else:
                price = price * Count
                break
        if price > self.wallet:
            print("You don't have enough money.")
            again = pyip.inputYesNo(prompt=" Do you want to increase your wallet balance? (y/n) ")
            if again == "n":
                self.show_data()
                return
            else:
                user = Transaction()
                print("Please enter the amount of money you want to deposit into your wallet.")
                depos = check_int()
                user.deposit(depos)
                if price <= self.wallet:
                    self.wallet -= price
        else:
            pass
