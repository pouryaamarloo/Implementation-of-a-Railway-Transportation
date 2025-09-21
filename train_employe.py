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
        pass

    def update_line(self):
        pass

    def delete_line(self):
        pass

    def list_line(self):
        pass

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
                     rate = self.rate,price = self.price,amount = self.amount,id = id_ )
        self.detail.append(dict_)
        print("اگر باز هم میخواهید اطلاعات قطار جدید ارائه دهید گزینه یک \nاگر میخواهد به پنل کارمند بروید گزینه 0")
        select_= pyip.inputInt(min= 0 , max =1)
        if select_ == 0:
            self.panel_employee()
            return
        else :
            self.add_train()
            return
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
            print("1.add line")
            print("2.update line")
            print("3.delete line")
            print("4.list line")
            print("5. add train")
            print("6. delete train")
            print("7. list train")
            answer = input()
            if answer == "1":
                self.add_line()
                break
            if answer == "2":
                self.update_line()
                break
            if answer == "3":
                self.delete_line()
                break
            if answer == "4":
                self.list_line()
                break
            if answer == "5":
                self.add_train()
                break
            if answer == "6":
                self.delete_train()
                break
            if answer == "7":
                self.list_train()
                break
            else :
                print("this number is out of range")
                print("try again")

            



