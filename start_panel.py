from admin_kol import ManagementPanel
from train_employe import *


def start_panel():
    '''
    Start Panel for Calling Different Panels
    such as Admin, Train Employee, and Regular User
    '''
    state = 0
    while True:
        print("""
1.Admin Panel
2.Employee Panel
3.Normal Panel
4.Exit
        """)
        user_input = input("please enter your choice: ")
        while True:
            if user_input == "1":

                user_name = input("please enter your user name: ")
                password = input("please enter your password: ")
                if user_name == "Admin_Train":  # اگر ورودی 1 بود و یوزر نیم صحیح بود وارد پنل ادمین کل شود
                    state = 1
                else:
                    print("Error wrong user name")  # در صورت اشتباه بودن یوزر نیم این پیام نمایش داده شود
                    continue
                if password == "Pass_Train" and state == 1:  #:اگر پسورد تعیین شده بود و یوزر نیم درست وارد شده بود
                    print("welcome to the Management Panel!")  # نمایش پیام خوش آمد گویی
                    admin = ManagementPanel()  # فراخوانی کلاس ادمین کل
                    admin.panel()
                    break
                else:
                    print("Error wrong password")  # در صورت اشتباه بودن پسورد پیام مقابل نمایش داده شود
                    continue
        if user_input == "2":
            while True:
                user_name = input()
                password = input()
                if not admin.employess():
                    print("we don't have enough employes!\n you should add employess first")
                    start_panel()
                    return

                for i in admin.employess():
                    if i["user_name"] == user_name and i["password"] == password:
                        print(f"welcome to the Management Panel!{i['name']}")
                        employee = Employee()
                        employee.panel_employee()
                        break

                    else :
                        print("Error wrong user name and password")
                        continue
                break
            return
        if user_input == "3":
            pass

start_panel()