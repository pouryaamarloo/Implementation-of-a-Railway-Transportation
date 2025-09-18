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
                admin = ManagementPanel()    # فراخوانی کلاس ادمین کل
                print("به پنل مدیریت خوش آمدید")
                
            else :
                print("Error wrong password")
                continue

class Employee:
    def __init__(self, name, family, username, password, email): #مشخصات کارمند ها مثل اسم و فامیل و یوزرنیم و پسورد و ایمیل توی این کلاس اورده شدن
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.email = email

class ManagementPanel:#کلاس پنل مدیریت
    def __init__(self):
        self.employees = []  # لیست کارمندها

    def panel(self):
        while True:
            print("1:add employee")
            print("2:remove employee")
            print("3:show employee's list")
            print("4:exit to start panel")
            choice=int(input())
            if choice==1:
                self.add_employee()
            elif choice ==2:
                self.remove_employee()
            elif choice ==3:
                self.list_employees()
            elif choice==4:
                break
            else:
                print("invalid choice")


    def add_employee(self):
        import re
        username = input(":لطفا یوزرنیم کارمند را وارد کنید")
        # بررسی تکراری بودن username
        for e in self.employees:
            if e.username == username:
                print("Error: یوزرنیم در حال حاضر وجود دارد")
                return
        password = input(":لطفا پسورد کارمند را وارد کنید")
        pass_pattern= r'^[A-Za-z0-9@&]+$'
        if not re.match(pass_pattern,password):
            print("password must includ :english alphabet,numbers ,@ or &")
            return
        email = input(":لطفا ایمیل کارمند را وارد کنید")
        email_pattern=r'^[a-zA-Z0-9_.+-]+@(gmail|yahoo)\.com$'
        if not re.match(email_pattern,email):
            print("the email must follow the correct format")
            return
        while True:   
            name = input(":لطفا اسم کارمند را وارد کنید")
            family = input(":لطفا فامیلی کارمند را وارد کنید")
            if not name.isalpha() or not family.isalpha():
                print("name or family name is invalid")

                choice=input("1 : mikhaham dobare vared konam ,2 : bargasht be panel")
                if choice == 1:
                   continue
                elif choice == 2:
                    break
        
            else:
                emp = Employee(name, family, username, password, email)
                self.employees.append(emp)
                print(f"کارمند {username}با موفقیت اضافه شد")#پیام اضافه کردن کارمند

    def remove_employee(self):
        username = input(":لطفا یوزرنیم کارمند را وارد کنید")
        # بررسی وجود username
        for e in self.employees:
            if e.username == username:
                self.employees.remove(e)
                print(f"کارمند {username}با موفقیت حذف شد")#پیام حذف کارمند
                return
        print("Error: !کارمند یافت نشد")

    def list_employees(self):
        if not self.employees:
            print("!کارمند یافت نشد")
        for e in self.employees:
            print(f"Username: {e.username}, Name: {e.name} {e.family}")
