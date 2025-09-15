def start_panel():
    '''
    پنل شروع جهت فراخوانی پنل های متفاوت از قبیل
    ادمین کل ، کارمند قطار، کاربر عادی
    '''
    state =0
    while True:
        print("1.ادمین کل")
        print("2.کارمند قطار")
        print("3.کاربر عادی")
        print("4.خروج")
        user_input = int(input())

        if user_input == 1:
            user_name = input()
            password = input()
            if user_name == "Admin_Train" :
                state = 1
            else :
                print("Error wrong user name")
                continue
            if password == "Pass_Train" and state == 1 :
                admin = Admin_Panel()    # فراخوانی کلاس ادمین کل
                print("خوش اومدی ادمین")
            else :
                print("Error wrong password")
                state = 0
                continue
        pass

