from bank import API
from test import exp_month
from train_employe import Employee
import pyinputplus as pyip
import datetime as dt

class Normal_User_Panel(Employee):
    def __init__(self):
        super().__init__()
        self.username ="pouryaam"
        self.User =[{
            "Name" : "pourya",
            "Email" : "pourya@gmail.com",
            "Username" : "pouryaam",
            "Password" : "123456#@",
            "card"    : {},
        }
        ]

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

class Buy_Ticket(Normal_User_Panel):
    def __init__(self):
        super().__init__()
        self.wallet = 500

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
                    train_amount = i['amount']
                    if Count > i['amount']:
                        print(
                            "The train capacity is less than what you selected\nif you want to back last panel enter 0")
                        Count = pyip.inputInt(
                            prompt="Please enter the number of tickets you want: \n if you want to back last panel enter 0 .",
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
                amount =user.deposit(num)
                self.wallet += amount
                print(f"Your wallet balance is {self.wallet}")

                if price <= self.wallet:
                    self.wallet -= price
                    print(f"Purchase completed successfully.your balance is {self.wallet}")
                    train_amount = train_amount - Count
                    for i in self.detail:
                        if choice == i['id']:
                            i.update({"amount":train_amount})

                            file = f""
                            self.show_data()
                            return
                else:
                    while True:
                        print("your balance is less than your ticket price. ")
                        again = pyip.inputYesNo(prompt=" Do you want to increase your wallet balance? (y/n) ")
                        if again == "n":
                            self.show_data()
                            break
                        else :
                            print("please enter the amount of money you want to deposit into your wallet.")
                            num = check_int()
                            amount =user.deposit(num)
                            self.wallet += amount
                            print(f"Your wallet balance is {self.wallet}")
                            if price <= self.wallet:
                                print("Purchase completed successfully")
                                self.show_data()
                                return
                            else :
                                continue



                    return

        else:
            self.wallet -= price
            print("Purchase completed successfully.")
            train_amount -= train_amount - Count
            for i in self.detail:
                if choice == i['id']:
                    i.update({"amount": train_amount})
                    self.show_data()
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
        for i in self.User :
            if  i["card"]  :
                card = i["card"]["card"]
                exp_month = i["card"]["exp_month"]
                exp_year = i["card"]["exp_year"]
                password = i["card"]["password"]
                cvv2 = i["card"]["cvv2"]
                Valid = API()
                flag = Valid.pay(card, exp_month, exp_year, password, cvv2, amount)
                if flag :
                    return amount



        card=input("Enter the card number: ")
        print("exp month :")
        exp_month =check_int()
        print("exp year :")
        exp_year = check_int()
        print("password :")
        password = check_int()
        print("cvv2 :")
        cvv2 = check_int()
        Valid = API ()
        flag = Valid.pay(card,exp_month,exp_year,password,cvv2,amount)
        if flag :

            for j in self.User:
                if j["Username"] == self.username:
                    j["card"].update({"card":card,"exp_month":exp_month,"exp_year":exp_year,"password":password ,"cvv2":cvv2})
            print(self.User)




            return amount

def create_file(list_):
    Count = 0
    for i in list_:
        Count += 1
        with open(f"file/{i['username']}") as f :
            f.write(f"")

pir = Buy_Ticket()
pir.show_data()
