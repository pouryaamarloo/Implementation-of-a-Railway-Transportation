import re  #استفاده از ریجکس برای بررسی ایمیل ،پسورد و یوزرنیم


class Normal_User_Panel :   #کلاس کاربران عادی
    def __init__(self):
        self.Users = []    #لیست ذخیره تمام کاربران ثبت شده
        self.Users_dict = {}    # دیکشنری برای دسترسی سریع به کاربران
        self.email_dict = {}
        self.username_dict = {}

    def acceptable_Email(self, email) :    #متد اعتبارسنجی ایمیل
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'    #بررسی میکند ایمیل مطابق الگو باشد
        return re.match(pattern, email)     #اگر ایمیل با شرایط مطابقت کرد شی مچ برمیگردد در غیر این صورت نان

    def acceptable_Password(self, password) :      #متد اعتبار سنجی پسورد
        pattern = r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@&]).{8,10}$'       #بررسی میکند پسورد مطابق الگو باشد
        return re.match(pattern, password)     #اگر یوزرنیم با شرایط مطابقت کرد شی مچ برمیگردد در غیر این صورت نان

    def acceptable_Username(self, username) :    #متد اعتبار سنجی یوزرنیم
        pattern = r'^[a-zA-Z0-9]{4,10}$'    #بررسی میکند یوزرنیم مطابق الگو باشد
        return re.match(pattern, username)    #اگر یوزرنیم با شرایط مطابقت کرد شی مچ برمیگردد در غیر این صورت نان


    def register(self) :   #متد ثبت نام
        while True :
            name = input("Name: ").strip()   #دریافت نام کاربر و حذف فاصله اضافه
            while True :
                email = input("Email: ").strip()    #دریافت ایمیل کاربر و حذف فاصله اضافه
                if not self.acceptable_Email(email) :    #اگر ایمیل نامعتبر باشد
                    print("Email is invalid!")   #پیام چاپ میشود
                    continue
                if email in self.email_dict :   #اگر ایمیل تکراری باشد
                    print("This email is already in use.")   #پیام چاپ میشود
                    continue
                break
            while True :
                username = input("Username: ").strip()   #دریافت یوزرنیم و حذف فاصله اضافه
                if not self.acceptable_Username(username) :   #اگر یوزرنیم نامعتبر باشد
                    print("Username must be 4-10 letters/numbers.")   #پیام چاپ میشود
                    continue
                if username in self.username_dict :   #اگر یوزرنیم تکراری باشد
                    print("This username is already in use.")   #پیام چاپ میشود
                    continue
                break
            while True :
                password = input("Password: ").strip()   #دریافت پسورد و حذف فاصله اضافه
                if not self.acceptable_Password(password) :    #اگر پسورد نامعتبر باشد
                    print("Password must be 8-10 chars, include letters, numbers, & or @.")   #پیام چاپ میشود
                    continue
                break

            #ساخت دیکشنری برای اطلاعات کاربر
            new_user = {
                'name' : name ,
                'email' : email ,
                'username' : username ,
                'password' : password
                }
            self.Users.append(new_user)   #کاربر جدید را به لیست اضافه میکند
            self.Users_dict[username] = new_user   #کاربر جدید را در دیکشنری مقابل ذخیره میکند
            self.email_dict[email] = True   #ایمیل کاربر را در دیکشنری مقابل ذخیره میکند
            self.username_dict[username] = True   #یوزرنیم کاربر را در دیکشنری مقابل ثبت میکند
            print("Registration successful!")   #چاپ پیام موفقیت
            while True :
                try :
                    choice = int(input("Add another user? 1:Yes  2:No: "))
                    if choice == 1 :
                        break
                    elif choice == 2 :
                        return
                    else :
                        print("Choose 1 or 2.")   #در صورت انتخاب عددی غیر از 1 و 2
                except ValueError :   #در صورت ورودی غیر عددی
                    print("Invalid input! Enter a number.")   #چاپ پیام ارور

    def login(self) :   #متد ورود
        while True :
            username = input("Username: ").strip()   #دریافت یوزرنیم و حذف فاصله اضافه
            password = input("Password: ").strip()   #دریافت پسورد و حذف فاصله اضافه

            user_found = self.Users_dict.get(username)   #دیکشنری است که یوزرنیم ها کلید و اطلاعات مقدارند
            if user_found and user_found['password'] == password :   #بررسی میکند کاربر پیدا شده و پسورد درست است
                print(f"Login successful! Welcome {user_found['name']}!")   #چاپ پیام موفقیت
                break
            else :   #در صورت عدم وجود یوزرنیم یا پسورد اشتباه
                print("Username or password is incorrect. Try again.")   #پیام خطا چاپ شده و حلقه دوباره اجرا میشود
                a =input("Press 1 to continue...\n if you want to back last panel enter 0 ")
                if a =="0" :
                    self.menu()
                    return
                if a == "1" :
                    continue
                else :
                    print("please enter again.")

        while True :
            select_user = input("Choose an option: 1. Back to Menu  2. Buy Ticket: ").strip()   #ورودی دریافت شده و فاصله های اضافی حذف میشوند
            if select_user == "1" :   #در صورت انتخاب گزینه یک
                self.menu()   # برگشت به منوی کاربر عادی
                return
            elif select_user == "2" :   #در صورت انتخاب گزینه دو
                                         # ورود به پنل خرید
                return
            else :
                print("Please choose 1 or 2")   #در صورت انتخاب اعداد غیر از این دو


    def menu(self) :   #متد منوی اصلی
        while True :
            print("\nMenu Options:\n1. Register\n2. Login\n3. Exit")
            try :
                user_choice = int(input("Choose (1-3) : ").strip())   #ورودی گرفته شده و فاصله های اضافی حذف میشود
                if user_choice == 1 :
                    self.register()   #رفتن به پنل ثبت نام
                elif user_choice == 2  :
                    self.login()
                    return          #رفتن به پنل ورود
                elif user_choice == 3 :
                    return   #خروج از برنامه
                else :
                    print("Choose a number between 1 and 3 .")   #پیام خطا در صورت ورودی غیر مجاز
                    return
            except ValueError :   #ارور در صورت ورودی غیر عددی
                print("Invalid input! Enter a number.")