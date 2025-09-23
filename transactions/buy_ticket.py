from bank import API
from train_employe import Employee
import pyinputplus as pyip
import datetime as dt
import re

class Normal_User_Panel(Employee):
    def __init__(self):
        super().__init__()
        self.username ="pouryaam"
        self.User =[{
            "name" : "pourya",
            "email" : "pourya@gmail.com",
            "username" : "pouryaam",
            "password" : "123456#@",
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
        self.wallet = 0
        self.tickets=[]

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

    def buy_ticket(self):


        def check_int():
            while True:
                try:
                    choice = int(input(""))
                except ValueError:
                    print("Please enter a number.")
                    continue
                if choice < 0 :
                    print("Please enter a positive number.")
                    continue
                if choice:
                    return choice

        def time_micro(now):
            now_no_micro = now.replace(microsecond=0)
            return now_no_micro

        user = Transaction()

        if not self.detail:
            print("You don't have any tickets to buy.")
            self.show_data()
            return
        for i in self.detail:

            with open("file/file.txt","w+") as f:
                f.write(f"""
                ==============================
                 Train Name : {i['train_name']}
                 Train ID   : {i['id']}
                 Line Name  : {i['line_name']}
                 Price      : {i['price']}
                 Capacity   : {i['amount']}
                ==============================
                """)
                f.seek(0)
                print(f.read())


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
        while True :
            if price > self.wallet:
                print(f"You don't have enough money. your balance is {self.wallet}")
                again = pyip.inputYesNo(prompt=" Do you want to increase your wallet balance? (y/n) ")
                if again == "n":
                    self.show_data()
                    return
                else:
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
                                time = dt.datetime.now()
                                time = time_micro(time)
                                dict_ =dict(user_name = self.username,train_name=i['train_name'],id=i['id'],line_name=i['line_name'],price=i['price'],Count=Count , time=time)
                                self.tickets.append(dict_)
                                STR=f"""
                                    Name       : {dict_['user_name']}
                                    Train Name : {dict_['train_name']}
                                    id         : {dict_['id']}
                                    line_name  : {dict_['line_name']}
                                    price      : {dict_['price']}
                                    count      : {dict_['Count']}
                                    time       : {dict_['time']}
                                    
                                """
                                with open("file/tickets.txt","w+") as f:
                                    f.write(STR)
                                    f.seek(0)
                                    f.read()

                                self.show_data()
                                return
                    else:
                            continue



    def edit_detail(self):
        def show_list_detail():#show list of information about user
            for i in self.User:
                if i['username'] == self.username:
                    print(f"""
                    Name : {i["name"]},
                    Email : {i["email"]},
                    Username : {i["username"]},
                    Password : {i['password']},                    """)
        def change_detail(title): # edit information
            for i in self.User:
                if title in i :
                    while True :
                        a = input("Apply the changes.")
                        if title == "email":
                            if re.match(r'^[a-zA-Z0-9_.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', a):
                                i.update({"email":a})
                                return
                            else:
                                print("Please enter a valid email address.")
                                continue
                        if title == "password":
                            regex = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[#\$])[A-Za-z0-9#$]+$'
                            if re.match(regex,a):
                                i.update({"password":a})
                                print("Operation completed successfully ")
                                return
                            else :
                                print("please enter a valid password.")
                                continue
                        else:
                            print(f"acceptable ")
                            i.update({title:a})
                            break
                else:
                    print(f"{title} not found.")
                    return
            return


        show_list_detail()
        while True:
            title= input("Which part do you want to change?")
            title = title.lower()
            if title == "username":
                print("you can't change the username")
                continue
            change_detail(title)
            again =input('Do you want to make more changes or return to the previous menu? (y/n)')
            again = again.lower()
            if again == "n":
                break
            if again == "y":
                continue
            else :
                print("Please enter a valid option.")
                continue
        self.show_data()
        return




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
                if a < 0 :
                    print("Please enter a positive number.")
                else:
                    return a
        for i in self.User :
            if  "card" in i   :
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
                if j["username"] == self.username:
                    j["card"] = {
                        "card": card,
                        "exp_month": exp_month,
                        "exp_year": exp_year,
                        "password": password,
                        "cvv2": cvv2
                    }

            return amount

def create_file(list_):
    Count = 0
    for i in list_:
        Count += 1
        with open(f"file/{i['username']}") as f :
            f.write(f"")

pir = Buy_Ticket()
pir.show_data()
