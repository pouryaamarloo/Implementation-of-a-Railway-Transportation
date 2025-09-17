from curses.ascii import isdigit
from logging import exception


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
        try :
            while True:
                self.train_name = input("Enter train name:\nexit ")
                if self.train_name == 'exit':
                    self.panel_employee()
                    break
                if self.train_name == "":
                    continue
                self.line_name = input("Enter line name:\nexit  ")
                if self.line_name not in self.list_lines:
                    print("line name is not exist")
                    while True:
                        self.line_name = input("Enter line name:\nexit  ")
                        if self.line_name  in self.list_lines:
                            break
                if self.line == "":
                    continue
                if self.line_name == "exit" :
                    self.panel_employee()
                    break
                self.speed =int(input("Enter speed:\nexit "))
        except exception as e :
                print(e)








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


