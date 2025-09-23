from admin_kol import ManagementPanel
from train_employe import *
from Normal_User_Panel import *
from transactions import *
from transactions.buy_ticket import Buy_Ticket

def start_panel():
    '''
    Start Panel for Calling Different Panels
    such as Admin, Train Employee, and Regular User
    '''
    admin = None   # تعریف اولیه تا بعداً مشکل نده
    employee = None

    while True:
        print("""
1.Admin Panel
2.Employee Panel
3.Normal Panel
4.Exit
        """)
        user_input = input("please enter your choice: ")

        if user_input == "1":
            user_name = input("please enter your user name: ")
            password = input("please enter your password: ")

            if user_name == "Admin_Train" and password == "Pass_Train":
                print("welcome to the Management Panel!")
                admin = ManagementPanel()
                admin.panel()
            else:
                print("Error: wrong username or password")

        elif user_input == "2":
            if not admin or not admin.employees:
                print("we don't have enough employees!\n you should add employees first")
                continue

            user_name = input("please enter your user name: ")
            password = input("please enter your password: ")

            for i in admin.all_information:
                if user_name == i["username"] and password == i["password"]:
                    employee = Employee()
                    employee.panel_employee()
                    break
            else:
                print("username or password incorrect")

        elif user_input == "3":
            user = Normal_User_Panel()
            user.menu()

            user_name = None
            for i in user.Users:
                if i.get("username"):
                    user_name = i["username"]
                    break

            if not user_name:
                print("you have no user name")
            else:
                if not employee:
                    print("Error: no employee available for detail")
                    continue

                detail = employee.detail
                wallet = Buy_Ticket(user.Users, user_name, detail)
                wallet.show_data()

        elif user_input == "4":
            print("Goodbye!")
            break






start_panel()