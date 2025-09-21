import re

class ManagementPanel:#کلاس پنل مدیریت
    def __init__(self):
        self.employees = []  # لیست کارمندها

    def add_employee(self):#متد اضافه کردن کارمند قطار
        while True:
            while True:#حلقه برای گرفتن یوزرنیم
                username = input("Enter username: ").strip()#یوزرنیم وارد میشود و فاصلخ اضافی ان حذف میشود
                if any(emp["username"] == username for emp in self.employees):#با استفاده از این تابع بررسی میشود که ایمیل وجود داشته یا نه
                    print("Error: Username already exists")#در صورت تکراری بودن پیام خطا چاپ میشودو ادامه میابد
                    continue_choice = self.retry_or_return()
                    if continue_choice == "return":
                        return
                    #اگر کاربر برگشت را انتخاب کند برگردد
                    else:#در غیر این صورت حلقه ادامه میابد
                        continue
                break
        
            while True:#حلقه گرفتن پسورد
                password = input("Enter password: ").strip()#پسورد وارد میشود و فاصله اضافی ان حذف میشود
                if not re.match(r'^[A-Za-z0-9@&]{6,16}$', password):
                #با استفاده از ریجکس بررسی میشود که پسورد شامل حروف انگلیسی عدد @ یا & باشد و طولش بین 6 تا 16 کاراکتر باشد    
                    print("Password must include letters, numbers, @ or & and length 6-16")# صدا زده میشود retry_or_return  در صورت خطا پیام چاپ شده و متد
                    continue_choice = self.retry_or_return()
                    if continue_choice == "return":
                        return
                    #اگر کاربر برگشت را انتخاب کند برگردد
                    else:#در غیر این صورت حلقه ادامه میابد
                        continue
                break

       
            while True:#حلقه گرفتن ایمیل
                email = input("Enter email: ").strip()#ایمیل وارد میشود و فاصله اضافی آن حذف میشود
                if any(emp["email"] == email for emp in self.employees):#بررسی میشود که ایمیل وجود داشته یا نه
                    print("Error: Email already exists")
                    continue
                if not re.match(r'^[a-zA-Z0-9_.+-]+@(gmail|yahoo)\.com$', email):#gmail/yahoo با استفاده از ریجکس بررسی میشود که ایمیل از دو فرمت رو به رو باشد
                    print("Email must be in correct format (gmail/yahoo)")#در صورت اشتباه پیام خطا چاپ میشود
                    continue_choice = self.retry_or_return()
                    if continue_choice == "return":#دوباره گزینه برگشت پرسیده شود 
                        return
                    else:#در غیر این صورت حلقه ادامه میابد
                        continue
                break

        
            while True:#حلقه گرفتن نام و نام خانوادگی
                name = input("Enter name: ").strip()#نام وارد شده و فاصله اضافه ان حذف میشود
                family = input("Enter family: ").strip()#نام خانوادگی وارد شده و فاصله اضافه ان حذف میشود
                if not name.isalpha() or not family.isalpha():#بررسی میکند که فقط حروف وارد شده باشد
                    print("Name and family must only contain letters")
                    continue_choice = self.retry_or_return()
                    if continue_choice == "return":#اگر  اشتباه بود همان روال برگشت اعمال میشود
                        return
                    else:
                        continue
                break

            # اضافه کردن کارمند به لیست
            emp = {
                "username": username,
                "password": password,
                "email": email,
                "name": name,
                "family": family
            }
            #بعد از وارد کردن تمام اطلاعات درست یک دیکشنری ساخته میشود که اطلاعات کارمند را نگه میدارد
            self.employees.append(emp)#دیکشنری ساخته شده به لیست کارمندان اضافه میشود
            print(f"Employee {username} added successfully.")#پیام اضافه شدن موفقیت آمیز کارمند نشان داده میشود
            while True:
                try:
                    repeat=input("do you want add another user? \n choose 1:yes \n if choose 2:no")
                    if repeat == 1:
                        break    
                    elif repeat ==2:
                        return
                    else:
                        print("Choose 1 or 2")
                except ValueError:
                    print("Invalid input! Enter a number.")



    def retry_or_return(self):#متد کمکی برای خروج یا تلاش دوباره
        while True:
            try:
                choice = int(input("1: retry  2: return to panel: "))#انتخاب 1 به معنای تلاش دوباره و 2 به معنای برگشت به پنل اصلی میباشد
                if choice == 1:
                    return "retry"
                elif choice == 2:
                    return "return"
                else:
                    print("Choose 1 or 2")#در صورت ورود عدد غیر از 1 و 2 درخواست میشود ورودی 1 یا 2 باشد
            except ValueError:#در صورت ورودی غیر عددی اکسپشن پرت شده و درخواست میشود عدد وارد شود
                print("Invalid input! Enter a number.")

    def remove_employee(self):#متد حذف کارمند قطار 
        username = input("Enter username to remove: ").strip()#گرفتن یوزر نیم جهت حذف کارمند و حذف فاصله اضافه
        for emp in self.employees:
            if emp["username"] == username:#اگر یوزرنیم وارد شده وجود داشت
                self.employees.remove(emp)#کارمند حذف میشود
                print(f"Employee {username} removed successfully.")#پیام موفقیت در حذف چاپ میشود
                return
        print("Error: Employee not found!")#اگر یوزر نیم پیدا نشد پیام نشان داده شود

    def list_employees(self):#متد نمایش تمام کارمندان
        if not self.employees:#اگر لیست خالی باشد
            print("No employees found.")#پیام نمایش داده شود
            return
        for emp in self.employees:#در غیر این صورت اطلاعات هر کارمند چاپ شود
            print(f"Username: {emp['username']}, Name: {emp['name']} {emp['family']}, Email: {emp['email']}")

    def panel(self):  # متد انتخاب پنل توسط کاربر
        while True:
            print("\n1: Add employee\n2: Remove employee\n3: Show employees\n4: Exit")#نمایش گزینه ها به کاربر 
            choice = input("Choose option: ").strip()#ورودی اعداد صحیح بین 1 تا 4 گرفته میشود

            if choice == "1":
                self.add_employee()#وارد پنل اضافه کردن کارمند میشود

            elif choice == "2":
                self.remove_employee()#وارد پنل حذف کارمند میشود

            elif choice == "3":
                self.list_employees()#وارد پنل اضافه کردن لیست میشود

            elif choice == "4":
                print("Exiting panel...")#از پنل ادمین کل خارج میشود
                return
            
            else:
                print("Invalid choice, enter 1-4")# در صورت ورود اعداد صحیح غیر از 1 تا 4 خواسته میشود عددی بین اینها وارد شود