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
        self.detail = [
            {   "train_name" : "306",
                "line_name"  : "mashhad_tehran",
                "speed"      : 120,
                "wait"        : 5 ,
                "rate"        : 5 ,
                "price" :      100 ,
                "amount"      : 200 ,
                "id"          : 3

            }
        ]

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
                print(f"""
                ==============================
                 Train Name : {i['train_name']}
                 Train ID   : {i['id']}
                 Line Name  : {i['line_name']}
                 Price      : {i['price']}
                 Capacity   : {i['amount']}
                ==============================
                """)
        while True:
            print("please enter train id ")
            choice = check_int()
            print("Please enter the number of tickets you want.")
            Count = check_int()
            price = 0
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
            print(f"You don't have enough money. your balance is {self.wallet}")
            again = pyip.inputYesNo(prompt=" Do you want to increase your wallet balance? (y/n) ")
            if again == "n":
                self.show_data()
                return
            else:
                user = Transaction()
                print("Please enter the amount of money you want to deposit into your wallet.")
                num = check_int()
                user.deposit(num)
                print(f"your wallet balance is {self.wallet}")
                if price <= self.wallet:
                    self.wallet -= price

        else:
            pass
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
                return
            if result == "2":
                self.edit_detail()
                return
            if result == "3":
                return
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


        card=input("Enter the card number: ")
        print("exp month :")
        exp_moth =check_int()
        print("exp year :")
        exp_year = check_int()
        print("password :")
        password = check_int()
        print("cvv2 :")
        cvv2 = check_int()
        Valid = API ()
        flag = Valid.pay(card,exp_moth,exp_year,password,cvv2,amount)
        if flag:
            self.wallet += amount
            print(f"your wallet balance is {self.wallet}")
            again = pyip.inputYesNo(prompt=" Do you want deposit again ? (y/n) ")

            if again == "Y":
                print("please enter the amount of money you want to deposit into your wallet.")
                amount = check_int()
                self.deposit(amount)

            else:
                return


pir = Buy_Ticket()
pir.show_data()
