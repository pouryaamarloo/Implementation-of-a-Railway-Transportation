class Employee:
    def __init__(self):
        pass


    def add_line(self):
        pass

    def update_line(self):
        pass

    def delete_line(self):
        pass

    def list_line(self):
        pass

    def add_train(self):
        pass

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


