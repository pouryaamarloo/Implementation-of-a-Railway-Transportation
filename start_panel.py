
def start_panel():
    '''
    پنل شروع جهت فراخوانی پنل های متفاوت از قبیل
    ادمین کل ، کارمند قطار، کاربر عادی
    '''
    state = 0
    while True:
        print("1.ادمین کل")
        print("2.کارمند قطار")
        print("3.کاربر عادی")
        print("4.خروج")
        user_input = input()

        if user_input == "1":
            user_name = input()
            password = input()
            if user_name == "Admin_Train":  # اگر ورودی 1 بود و یوزر نیم صحیح بود وارد پنل ادمین کل شود
                state = 1
            else:
                print("Error wrong user name")  # در صورت اشتباه بودن یوزر نیم این پیام نمایش داده شود
                continue
            if password == "Pass_Train" and state == 1:  #:اگر پسورد تعیین شده بود و یوزر نیم درست وارد شده بود
                print("welcome to the Management Panel!")  # نمایش پیام خوش آمد گویی
                admin = ManagementPanel()  # فراخوانی کلاس ادمین کل
                admin.panel()
                continue

            else:
                print("Error wrong password")  # در صورت اشتباه بودن پسورد پیام مقابل نمایش داده شود
                continue
        if user_input == "2":
            while True:
                user_name = input()
                password = input()
                for i in admin.employess():
                    if i["user_name"] == user_name and i["password"] == password:
                        print(f"welcome to the Management Panel!{i['name']}")
                        employee = Employe()
                        employee.panel_employee()
                        break

                    else :
                        print("Error wrong user name and password")
                        continue
        if user_input == "3":
            pass

