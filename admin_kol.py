import re

class ManagementPanel:#کلاس پنل مدیریت
    def __init__(self):
        self.employees = []  # لیست کارمندها
        self.all_information = []

    def add_employee(self):#متد پنل اضافه کردن کارمند قطار
        while True :

            username = input("Please enter the employee's username:")#دریافت یوزرنیم از کاربر

            # بررسی تکراری بودن username
            if username in self.employees:
                print("Employee with that username already exists")
                continue
            else :
                self.employees.append(username)
                break


        while True:
            password = input("Please enter the employee's password:")  # دریافت پسورد از کاربر
            pass_pattern= r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[#\$])[A-Za-z0-9#$]+$'
            if not re.match(pass_pattern,password):
                print("password must includ :english alphabet,numbers ,@ or & \n and password length must be between 6 and 16 characters")
                select=int(input("1 : please enter your password again \n 2 : return to the panel"))
                if select==1:
                    continue
                elif select==2:
                    self.panel()
                    return
                elif select!= 1 and select!=2:
                    print("please choose between option 1 and 2")
                    continue
                else:
                    break
            else :
                break
        while True:
            email = input("Please enter the employee's email:")
            for i in self.all_information:
                if email == i['email']:
                     print("Error: The username already exists")
                     return#خروج از متد در صورت تکراری

            email_pattern=r'^[a-zA-Z0-9_.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern,email):
                print("the email must follow the correct format")
                select=int(input("1 : please enter your email again \n 2 : return to the panel"))
                if select==1:
                    continue
                elif select==2:
                    self.panel()
                elif select!= 1 and select!=2:
                    print("please choose between option 1 and 2")
                    continue
                else:
                    break
            else:
                break
        while True:
            name = input("Please enter the employee's name:")
            family = input("Please enter the employee's family name:")
            if not name.isalpha() or not family.isalpha():
                print("name or family name is invalid")

                choice=int(input("1 : mikhaham dobare vared konam ,2 : bargasht be panel"))
                if choice == 1:
                   continue
                elif choice == 2:
                    break
            else :
                break

        dict_=dict(username=username,password=password,email=email,name=name,family=family)
        self.all_information.append(dict_)
        print(f"Employee {username} successfully added.")#پیام اضافه کردن کارمند
        while True:
            again = input("Do you want to try again or go to the main panel? (y/n)")
            again = again.lower()
            if again == "y":
                break
            if again == "n":
                self.panel()
                return
            else:
                continue
        self.add_employee()

    def remove_employee(self):
        while True:
            username = input("Please enter the employee's username:")
            # بررسی وجود username
            for i in self.all_information:
                if username == i['username']:
                    self.all_information.remove(i)
                    print(f"Employee {username} has been successfully deleted")#پیام حذف کارمند
                    self.panel()
                    return

            print("Error: Employee not found!")

            while True:
                again = input("Do you want to try again or go to the main panel? (y/n)")
                again=again.lower()
                if again == "y" :
                    break
                if again == "n" :
                    self.panel()
                    return
                else :
                    continue


    def list_employees(self):
        if not self.employees:
            print("Employee not found!")
            self.panel()
            return
        for e in self.all_information:
            print(f"Username: {e["username"]}, Name: {e["name"]} {e["family"]}")
        self.panel()
        return
    def panel(self):  # متد انتخاب پنل توسط کاربر
        while True:
            print("1:add employee")
            print("2:remove employee")
            print("3:show employee's list")
            print("4:exit to start panel")

            choice = input()
            if choice == "1":  # اگر عدد 1 وارد شد
                self.add_employee()  # باز شدن پنل اضافه کردن کارمند قطار
                break

            elif choice == "2":  # اگر عدد 2 وارد شد
                self.remove_employee()  # باز شدن پنل حذف کارمند قطار
                break

            elif choice == "3":  # اگر عدد 3 وارد شد
                self.list_employees()  # باز شدن پنل نمایش لیست کارمندان قطار
                break
            elif choice == "4":  # اگر عدد 4 وارد شد
                break  # خروج از پنل مدیریت

            else:
                print("invalid choice")  # در صورت انتخاب اعداد غیر از اعداد 1 تا 4 این پیام نمایش داده شود
