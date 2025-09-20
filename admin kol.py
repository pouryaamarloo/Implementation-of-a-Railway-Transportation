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
            if user_name == "Admin_Train" :#اگر ورودی 1 بود و یوزر نیم صحیح بود وارد پنل ادمین کل شود
                state = 1
            else :
                print("Error wrong user name")#در صورت اشتباه بودن یوزر نیم این پیام نمایش داده شود
                continue
            if password == "Pass_Train" and state == 1 :#:اگر پسورد تعیین شده بود و یوزر نیم درست وارد شده بود 
                admin = ManagementPanel()    # فراخوانی کلاس ادمین کل
                print("welcome to the Management Panel!")#نمایش پیام خوش آمد گویی 
                
            else :
                print("Error wrong password")#در صورت اشتباه بودن پسورد پیام مقابل نمایش داده شود
                continue

class Employee:
    def __init__(self, name, family, username, password, email): #مشخصات کارمند ها مثل اسم و فامیل و یوزرنیم و پسورد و ایمیل توی این کلاس اورده شدن
        self.name = name#تعریف آرگمان ها
        self.family = family
        self.username = username
        self.password = password
        self.email = email

class ManagementPanel:#کلاس پنل مدیریت
    def __init__(self):
        self.employees = []  # لیست کارمندها

    def panel(self):#متد انتخاب پنل توسط کاربر
        while True:
            print("1:add employee")
            print("2:remove employee")
            print("3:show employee's list")
            print("4:exit to start panel")
            
            choice=int(input())
            if choice==1:#اگر عدد 1 وارد شد
                self.add_employee()#باز شدن پنل اضافه کردن کارمند قطار
            
            elif choice ==2:#اگر عدد 2 وارد شد
                self.remove_employee()#باز شدن پنل حذف کارمند قطار
            
            elif choice ==3:#اگر عدد 3 وارد شد
                self.list_employees()#باز شدن پنل نمایش لیست کارمندان قطار
            
            elif choice==4:#اگر عدد 4 وارد شد
                break#خروج از پنل مدیریت
            
            else:
                print("invalid choice")#در صورت انتخاب اعداد غیر از اعداد 1 تا 4 این پیام نمایش داده شود


    def add_employee(self):#متد پنل اضافه کردن کارمند قطار
        import re
        username = input("Please enter the employee's username:")#دریافت یوزرنیم از کاربر
        
        # بررسی تکراری بودن username
        for e in self.employees:
            if e.username == username:
                print("Error: The username already exists")
                return#خروج از متد در صورت تکراری بودن
            
        password = input("Please enter the employee's password:")  # دریافت پسورد از کاربر
        pass_pattern= r'^[A-Za-z0-9@&]+$'
        if not re.match(pass_pattern,password):
            print("password must includ :english alphabet,numbers ,@ or &")
            return
        email = input("Please enter the employee's email:")
        email_pattern=r'^[a-zA-Z0-9_.+-]+@(gmail|yahoo)\.com$'
        if not re.match(email_pattern,email):
            print("the email must follow the correct format")
            return
        while True:   
            name = input("Please enter the employee's name:")
            family = input("Please enter the employee's family name:")
            if not name.isalpha() or not family.isalpha():
                print("name or family name is invalid")

                choice=input("1 : mikhaham dobare vared konam ,2 : bargasht be panel")
                if choice == "1":
                   continue
                elif choice == "2":
                    break
        
            else:
                emp = Employee(name, family, username, password, email)
                self.employees.append(emp)
                print(f"Employee {username} successfully added.")#پیام اضافه کردن کارمند

    def remove_employee(self):
        username = input("Please enter the employee's username:")
        # بررسی وجود username
        for e in self.employees:
            if e.username == username:
                self.employees.remove(e)
                print(f"Employee {username} has been successfully deleted")#پیام حذف کارمند
                return
        print("Error: Employee not found!")

    def list_employees(self):
        if not self.employees:
            print("Employee not found!")
        for e in self.employees:
            print(f"Username: {e.username}, Name: {e.name} {e.family}")
