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

                dict_ =dict(line_name=self.line_name, start=self.start, end=self.end, total=self.total , Count=self.Count,distance=dist)
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
                    new_end = input("نام ایستگاه مقصد جدید: ")

                    for i in self.line_details:
                        if i["line_name"] == self.line_name:
                            i.update({"end":new_end})
                elif feature_choice == "3":
                    try:
                        self.Count = int(input("تعداد ایستگاه‌ها (به جز مبدأ و مقصد): "))
                    except ValueError:
                        print("لطفاً یک عدد صحیح وارد کنید.")
                        continue

                    for i in self.line_details:
                        if i["line_name"] == self.line_name:
                            i.update({"Count":self.Count})

                else:
                    print("گزینه نامعتبر!")
            elif choice == "2":
                    print("بازگشت به منوی کارمند.")
                    break
            else:
                    print("گزینه نامعتبر! لطفاً دوباره تلاش کنید.")


    def delete_line(self):
         while True:
            print("\n--- حذف خط ---")
            print("1. حذف خط")
            print("2. بازگشت به منوی کارمند")
            choice = input("انتخاب کنید: ")

            if choice == "1":
                line_name = input("نام خطی که می‌خواهید حذف کنید: ")

                if line_name not in self.lines:
                    print("خطی با این نام وجود ندارد! لطفاً نام صحیح وارد کنید.")
                    continue

                for i in self.line_details:
                    if i["line_name"] == self.line_name:
                        del self.line_details[i]

            elif choice == "2":
                print("بازگشت به منوی کارمند.")
                break
            else:
                print("گزینه نامعتبر! لطفاً دوباره تلاش کنید.")


    def list_line(self):
         while True:
            print("\n--- حذف خط ---")
            print("1. حذف خط")
            print("2. بازگشت به منوی کارمند")
            choice = input("انتخاب کنید: ")

            if choice == "1":
                line_name = input("نام خطی که می‌خواهید حذف کنید: ")

                if line_name not in self.lines:
                    print("خطی با این نام وجود ندارد! لطفاً نام صحیح وارد کنید.")
                    continue

                for i in self.line_details:
                    if i["line_name"] == self.line_name:
                        a = f"""
                            line_name : {i["line_name"]}
                            start     : {i["start"]}
                            end       : {i["end"]}
                            Count     : {i["Count"]}
                            total     : {i["total"]}
                        """
                        print(a)
            elif choice == "2":
                print("بازگشت به منوی کارمند.")
                break
            else:
                print("گزینه نامعتبر! لطفاً دوباره تلاش کنید.")


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
                    print("برای خروج عدد صفر را وارد کنید :")
                    adad = int(input())
                    if adad < 0 :
                        print("عدد باید مثبت باشه ")
                        continue
                except :
                    print("لطفا عدد وارد کنید :")
                    continue
                if type(adad) == int :
                    return adad
        print("لطفا نام قطار را وارد کنید : ")
        self.train_name = check_Str()
        if self.train_name == "exit":
            self.train_name = ""
            self.panel_employee()
        print("لطفا خط حرکت را وارد کنید :")
        while True:
            self.line_name = check_Str()
            if self.line_name not in self.list_lines :
                print("خط مورد نظر وجود ندارد :")
            else :
                break
        print("سرعت متوسط را وارد کنید :")
        self.speed = check_int()
        if self.speed == 0 :
            self.panel_employee()
        print("میزان توقف در هر ایستکاه را وارد کنید :")
        self.wait = check_int()
        if self.wait == 0 :
            self.panel_employee()
        print("لطفا کیفیت قطار را بین 1 تا 5 ستاره انتخاب کنید\nبرای خروج گزینه 0 را وارد کنید :")
        self.rate = pyip.inputInt(min= 0 , max =5)
        if self.rate == 0 :
            self.panel_employee()
        print("هزینه قطار را وارد کنید :")
        self.price = check_int()
        if self.price == 0 :
            self.panel_employee()
        print("لطفا ظرفیت را وارد کنید :")
        if self.amount == 0 :
            self.panel_employee()
        self.id_ += 1

        dict_ = dict(train_name = self.train_name,line_name = self.line_name,
                     speed = self.speed,wait = self.wait,
                     rate = self.rate,price = self.price,amount = self.amount,id = self.id_ )
        self.detail.append(dict_)
        print("اگر باز هم میخواهید اطلاعات قطار جدید ارائه دهید گزینه یک \nاگر میخواهد به پنل کارمند بروید گزینه 0")
        select_= pyip.inputInt(min= 0 , max =1)
        if select_ == 0:
            self.panel_employee()
            return
        else :
            self.add_train()
            return
    def update_train(self):
        pass

    def delete_train(self):
        list_ = []
        while True:
            try:
                id_ = int(input("لطفا ایدی قطار مورد نظر را وارد کنید\nاگر قصد بازگشت دارید عدد 0 را وارد کنید"))
            except :
                print("آیدی حتما باید عدد باشد دوست عزیز !!!")
                continue
            for i in self.detail:
                list_.append(i["id"])
            if id_ not in  list_ :
                print("آیدی که ووارد کردید وجود خارجی ندارد لطفا دوباره تلاش کنید")
            else :
                break
        for i in self.detail :
            if i["id"] == id_ :
                self.detail.remove(i)
                return


    def list_train(self):
        print(self.detail)
        while True:
            try:
                a = int(input("اگر قصد خروج دارید عدد صفر را وارد کنید "))
            except :
                print("لطفا فقط عدد وارد کنید")
            if a == 0:
                self.panel_employee()
                break
            else:
                print("لطفا مقدار صحیح را وارد کنید")


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

            



