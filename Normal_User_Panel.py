import re #چون باید باید از Regex استفاده بشه

class Normal_User_Panel():
    def __init__(self):
        self.name = ""
        self.email = ""
        self.username = ""
        self.password = ""

        self.Users = [] #برای ذخیره کردن کاربر
    #باید قبل از گرفتن اطلاعات با ریجکس ایمیل و یوزرنیم و پسورد رو بررسی کنیم
    def Acceptable_Email(email) :
        patern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        correct_email = re.match(patern , email)
        return correct_email
    
    def Acceptable_Password(password) :
        patern = r'^(?=.*[a-zA-z])(?=.*\d)(?=.*[@&]){8 , 10}'
        correct_pass = re.match(patern , password)
        return correct_pass
    
    def Acceptable_Username(username) :
        patern = r'^(?=.*[a-zA-z])(?=.*\d){4 , 10}$'
        correct_username = re.match(patern , username)
        return correct_username
    
    
    def Register(self) :
        print("\n*REGISTER*")
        
        while True :
            self.name = ""
            name = input("Name :")
            
            email = input("Email :")
            if not Acceptable_Email(email) :
                print("Email is invalid!")
                continue
        
            username = input("Username :")
            if not Acceptable_Username(username) :
                print("Your username must contain letters and numbers and be at least 4 characters long.")
                continue

            password = input("Password :")
            if not Acceptable_Password(password) :
                print("Your password must be 8 to 10 characters long and include both letters and numbers, and contain either **&** or **@**.")
                continue
            
            #تکراری بودن ایمیل و یوزر بررسی بشه!!
    def Login(self) :
        print("\n*Login*")
        while True :
            self.username = ""
            username = input("Username :")
            self.password = ""
            password = input("Password :")
            #باید بررسی کنیم که آیا کاربری وجود دارد یا نه
            karbar = None
            #درست بودن یوزر نیم و پسورد را بررسی میکنیم
            for user in self.Users :
                if user.username == username and user.password == password :
                    karbar = user
                    break
            if karbar is not None :
                print("Login successful! Welcome!")
                break
            else :
                print("The username or password is incorrect. Please try again.")



    def Menu(self):
        while True : #تا زمانی که دکمه بازگشت نخوره این حلقه ادامه داره
            ("Register , \nLogin , \nBack")
            user_choice = input() #کاربر باید از بین 3 گزینه منو یکی را انتخاب کنه
            if user_choice == "Register" :
                Register()
            elif user_choice == "Login" :
                Login()
            elif user_choice == "Back" :
                break
            
             