from curses.ascii import isdigit
from logging import exception
import pyinputplus as pyip



class Employee:
    def __init__(self):
        self.line_name = ""
        self.start = ""
        self.end = ""
        self.Count = 0
        self.list_lines = []

        self.train_name = ""
        self.line = ""
        self.speed = 0
        self.wait = 0
        self.rate = 0
        self.price = 0
        self.amount = 0


    def add_line(self):
        pass

    def update_line(self):
        pass

    def delete_line(self):
        pass

    def list_line(self):
        pass

    def add_train(self):
        def check_Str():
            while True:
                name = input()
                if name.isdigit():
                    print("لطفا اطلاعات درست وارد کنید")
                else :
                    return name
        def check_int():
            while True:
                try :
                    adad = int(input())
                except :
                    print("لطفا عدد وارد کنید ")
                    continue
                if type(adad) == int :
                    return adad
        print("لطفا نام قطار را وارد کنید ")
        self.train_name = check_Str()
        print("لطفا خط حرکت را وارد کنید")
        while True:
            self.line_name = check_int()
            if self.line_name not in self.list_lines :
                print("خط مورد نظر وجود ندارد")
            else :
                break
        print("سرعت متوسط را وارد کنید")
        self.speed = check_int()
        print("میزان توقف در هر ایستکاه را وارد کنید")
        self.wait = check_int()
        self.rate = pyip.inputInt("کیفیت قطار را از 1تا5 انتخاب کنید: ", min=1, max=5)


    def delete_train(self):
        pass

    def list_train(self):
        pass

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



pourya = Employee()
pourya.panel_employee()

