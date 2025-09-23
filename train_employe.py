from logging import exception
import pyinputplus as pyip

class Employee():
    def __init__(self):
        self.line_name = ""
        self.start = ""
        self.end = ""
        self.total = 0
        self.Count = 0
        self.list_lines = []
        self.lines = []
        self.line_details = []


        self.train_name = ""
        self.line = ""
        self.speed = 0
        self.wait = 0
        self.rate = 0
        self.price = 0
        self.amount = 0
        self.detail = []
        self.list_id=[]
        self.id_= 300

    def add_line(self):

        def check_int():
            while True :
                try:
                    num = int(input())
                    if num < 0 :
                        print("Please enter a possitive number")
                        continue
                except:
                    print("please enter a number")
                    continue
                return num
        def chek_str():
            while True :
                STR=input()
                if STR == "0":
                    self.panel_employee()
                    return
                if STR.isdigit() :
                    continue
                else :
                    return STR



        while True:
            print("\n--- Add a new line---")
            print("1. define new line")
            print("2.Return to the employee menu")
            choice = input(" choose: ")


            if choice == "1":
                self.line_name = input("Enter the name of the new line: ")

                if self.line_name in self.lines:
                    print("There is another line with this name. Please enter another name.")
                    continue
                else:
                    self.lines.append(self.line_name)
                print("please enter start")
                self.start = chek_str()
                print("please enter end")
                self.end = chek_str()

                print("please enter Counter of station")
                self.Count = check_int()
                list_lines = []
                for i in range(self.Count):
                    station_name = input(f" station name :")
                    list_lines.append(station_name)


                #total_distance = 0
                print("please enter distacne between 2 stations ")
                dist=check_int()
                print("please enter distance ")
                self.total = check_int()
                dict_ =dict(line_name=self.line_name, start=self.start, end=self.end, total=self.total , Count=self.Count,station=dist,list_station=list_lines)
                self.line_details.append(dict_)
                print(f"line  '{self.line_name}' Successfully registered.")

            elif choice == "2":
                print("Return to the employee menu.")
                break
            else:
                print("Invalid option! Please try again.")



    def update_line(self):
         while True:
            print("\n--- Line Editing---")
            print("1. line edite")
            print("2. Return to the employee menu")
            choice = input("Choose please : ")

            if choice == "1":
                self.line_name = input("نام خط مورد نظر برای ویرایش: ")

                if self.line_name not in self.lines:
                    print("There is no line with this name. Please enter a valid name.")
                    continue

                for i in self.line_details:
                    if i["line_name"] == self.line_name:
                        f= f"""
line_name : {i["line_name"]}
start     : {i["start"]}
end       : {i["end"]}
total     : {i["total"]}
Count     : {i["Count"]}
station     : {i["station"]}
list_station  : {i["list_station"]}
                            """
                        print(f)
                print("\nWhich feature do you want to edit?")
                print("1. Start")
                print("2. End ")
                print("3. Stations")
                feature_choice = input (" Your choose :")

                if feature_choice == "1":
                    new_start = input("نام ایستگاه مبدأ جدید: ")
                    for i in self.line_details:
                        if i["line_name"] == self.line_name:
                            i.update({"start":new_start})


                elif feature_choice == "2":
                    new_end = input(" New origin station name : ")

                    for i in self.line_details:
                        if i["line_name"] == self.line_name:
                            i.update({"end":new_end})
                elif feature_choice == "3":
                    try:
                        self.Count = int(input("Number of stations (excluding origin and destination):"))
                    except ValueError:
                        print("Please enter a valid number.")
                        continue

                    for i in self.line_details:
                        if i["line_name"] == self.line_name:
                            i.update({"Count": self.Count})

                else:
                    print("Invalid option")
            elif choice == "2":
                    print("Return to the employee menu.")
                    break
            else:
                    print("Invalid option! Please try again.")


    def delete_line(self):
         while True:
            print("\n----  Delet line  ---")
            print("1. Delet line")
            print("2. Return to emploee menu")
            choice = input (" Choose pls : ")

            if choice == "1":
                line_name = input("The name of the line you want to delete:")

                if line_name not in self.lines:
                    print("There is no line with this name! Please enter the correct name.")
                    continue

                for i in self.line_details:
                    if i["line_name"] == self.line_name:
                         self.line_details.remove(i)

            elif choice == "2":
                print("Return to emploee menu")
                break
            else:
                print("Invalid option! Please try again.")

    def list_line(self):
         while True:
            print("\n--  List Line ---")
            print("1.   Show list line ")
            print ("2. Return to  ")
            choice = input("Your choose : ")

            if choice == "1":

                for i in self.line_details:
                        a = f"""
                            line_name : {i["line_name"]}
                            start     : {i["start"]}
                            end       : {i["end"]}
                            Count     : {i["Count"]}
                            total     : {i["total"]}
                        """
                        print(a)
            elif choice == "2":
                print("returen to employee menu")
                break
            else:
                print("Invalid option! Please try again.")

    def add_train(self):
        def check_Str():#حساب کردن ورودی های رشته ای
            while True:
                print("برای خروج exit را تایپ کنید :")
                name = input()
                if name == "":
                    print("لطفا اطلاعات وارد کنید خالی نگذارید ")
                    continue
                if name.isdigit():
                    print("لطفا اطلاعات درست وارد کنید :")
                else :
                    return name
        def check_int():#حساب کردن ورودی های عددی
            while True:
                try :
                    print("if you want to back last panell enter 0")
                    adad = int(input())
                    if adad < 0 :
                        print("please enter a possitive number ")
                        continue
                except :
                    print("please enter a number")
                    continue
                if type(adad) == int :
                    return adad
        print("please enter train name ")
        self.train_name = check_Str()
        if self.train_name == "exit":
            self.train_name = ""
            self.panel_employee()
        print("please enter line name ")
        for i in self.detail:
            print(i["line_name"])
        while True:
            self.line_name = check_Str()
            if self.line_name not in self.lines :
                print("line_name does not exist")
            else :
                break
        print("please enter speed")
        self.speed = check_int()
        if self.speed == 0 :
            self.panel_employee()
        print("please enter wait")
        self.wait = check_int()
        if self.wait == 0 :
            self.panel_employee()
        print("please enter rate \n if you want to back last panell enter 0")
        self.rate = pyip.inputInt(min= 0 , max =5)
        if self.rate == 0 :
            self.panel_employee()
        print("please enter cost of train")
        self.price = check_int()
        if self.price == 0 :
            self.panel_employee()
        print("please enter amount of train")
        if self.amount == 0 :
            self.panel_employee()
        self.id_ += 1
        self.list_id.append(self.id_)


        dict_ = dict(train_name = self.train_name,line_name = self.line_name,
                     speed = self.speed,wait = self.wait,
                     rate = self.rate,price = self.price,amount = self.amount,id = self.id_ )
        self.detail.append(dict_)
        print("if you want to add new train enter 1 or back last panell enter 0")
        select_= pyip.inputInt(min= 0 , max =1)
        if select_ == 0:
            self.panel_employee()
            return
        else :
            self.add_train()
            return
    def update_train(self):

        def check_int():
            while True :
                try:
                    num = int(input())
                    if num < 0 :
                        print("Please enter a possitive number")
                        continue
                except:
                    print("please enter a number")
                    continue
                return num
        while True:
            print("\n--- Train Editing---")
            print("1. train edite")
            print("2. Return to the employee menu")
            choice = input("Choose please : ")

            if choice == "1":
                self.id_ = input("please enter train id ")

                if self.line_name not in self.list_id:
                    print("There is no line with this name. Please enter a valid name.")
                    continue

                for i in self.detail:
                    if i["id"] == self.id_:
                        f = f"""
        train_name    : {i["train_name"]}
        line_name     : {i["line_name"]}
        speed         : {i["speed"]}
        wait          : {i["wait"]}
        rate          : {i["rate"]}
        price         : {i["price"]}
        amount        : {i["amount"]}
        list_station  : {i["list_station"]}
                                    """
                        print(f)
                print("\nWhich feature do you want to edit?")
                print("1. train_name")
                print("2. line_name ")
                print("3. speed")
                print("4. wait")
                print("5. rate ")
                print("6. price")
                print("7. amount")

                while True:

                    feature_choice = input(" Your choose :")

                    if feature_choice == "1":
                        new_start = input("please enter train name ")
                        for i in self.detail:
                            if i["id"]==self.id_ :
                                i.update({"train_name": new_start})
                                break
                    if feature_choice == "2":
                        new_start = input("please enter line name ")
                        for i in self.line_details:
                            if i["id"] == self.id_ :
                                i.update({"line_name": new_start})
                                break

                    if feature_choice == "3":
                        print("please enter speed ")
                        new_speed = check_int()
                        for i in self.line_details:
                            if i["id"] == self.id_:
                                i.update({"speed": new_speed})
                                break

                    if feature_choice == "4":
                        print("please enter wait ")
                        new_start = check_int()
                        for i in self.line_details:
                            if i["id"] == self.id_:
                                i.update({"wait": new_start})
                                break

                    if feature_choice == "5":
                        print("please enter rate ")
                        new_start = check_int()
                        for i in self.line_details:
                            if i["id"] == self.id_:
                                i.update({"rate": new_start})
                                break
                    if feature_choice == "6":
                        print("please enter price ")
                        new_start = check_int()
                        for i in self.line_details:
                            if i["id"] == self.id_:
                                i.update({"price": new_start})
                                break


                    if feature_choice == "7":
                        print("please enter amount ")
                        new_start = check_int()
                        for i in self.line_details:
                            if i["id"] == self.id_:
                                i.update({"amount": new_start})
                                break
                    else :
                        print("please enter correct Value ")





    def delete_train(self):
        while True:
            try:
                print("Please enter the ID of the desired train.")
                print("If you want to go back, enter 0.")
                id_ = int(input())
            except :
                print("please enter correct Value ")
                continue
            if id_ == 0 :
                break
            for i in self.detail:
                if i["id"] == id_:
                    self.detail.remove(i)
        return




    def list_train(self):
        for i in self.detail:
            if i["line_name"] == self.line_name:
                f = f"""
        train_name: {i["train_name"]}        
        line_name : {i["line_name"]}
        speed     : {i["speed"]}
        wait      : {i["wait"]}
        rate      : {i["rate"]}
        price     : {i["price"]}
        amount    : {i["amount"]}
        id        : {i["amount"]}
                                    """
                print(f)
        while True:
            try:
                a = int(input("if you want to back last panell enter 0"))
            except :
                print("please enter a possitive number ")
            if a == 0:
                self.panel_employee()
                break
            else:
                print("please enter number ")


    def panel_employee(self):
        while True:
            print("""
1.Add Line
2.Update Line
3.Delete Line
4.Show Line List
5.Add Train
6.Update Train
7.Delete Train
8.Show Train List
9.Exit            
            """)

            answer = input()
            if answer == "1":
                self.add_line()
                continue
            if answer == "2":
                self.update_line()
                continue
            if answer == "3":
                self.delete_line()
                continue
            if answer == "4":
                self.list_line()
                continue
            if answer == "5":
                self.add_train()
                continue
            if answer == "6":
                self.update_train()
                continue
            if answer == "7":
                self.delete_train()
                continue
            if answer == "8":
                self.list_train()
            if answer == "9":
                return
            else :
                print("this number is out of range")
                print("try again")





