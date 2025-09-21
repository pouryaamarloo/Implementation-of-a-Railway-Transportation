import re #چون باید باید از Regex استفاده بشه

class Normal_User_Panel():
    def __init__(self):
        self.name = ""
        self.email = ""
        self.username = ""
        self.password = ""

        self.Users = [] #برای ذخیره کردن کاربر
    #باید قبل از گرفتن اطلاعات با ریجکس ایمیل و یوزرنیم و پسورد رو بررسی کنیم
    def acceptable_Email(email) :
        patern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        correct_email = re.match(patern , email)
        return correct_email
    
    def acceptable_Password(password) :
        patern = r'^(?=.*[a-zA-z])(?=.*\d)(?=.*[@&]){8,10}'
        correct_pass = re.match(patern , password)
        return correct_pass
    
    def acceptable_Username(username) :
        patern = r'^(?=.*[a-zA-z0-9]{4,10}$'
        correct_username = re.match(patern , username)
        return correct_username

    
    
    def Register(self) :
        print("\n*REGISTER*")
        
        email_dict = {}
        username_dict = {}
        
        while True :
            self.name = input("Name :")
            
            self.email = input("Email :")
            if not acceptable_Email(self.email) :
                print("Email is invalid!")
                continue

            if self.email in email_dict : #تکراری بودن ایمیل بررسی میشه
                print("This email is already in use.")
                continue
        
            self.username = input("Username :")
            if not acceptable_Username(self.username) :
                print("Your username must contain letters and numbers and be at least 4 characters long.")
                continue

            if self.username in username_dict : #تکراری بودن یوزرنیم بررسی میشه
                print("This username is already in use.")
                continue

            self.password = input("Password :")
            if not acceptable_Password(self.password) :
                print("Your password must be 8 to 10 characters long and include both letters and numbers, and contain either (&) or (@).")
                continue

            new_user = {
                'Name' : self.name , 
                'Email' : self.email , 
                'Username' : self.username , 
                'Password' : self.password
                }  #برای ثبت کردن کاربر جدید
            
            self.Users.append(new_user) 
            
        #حالا باید برای اینکه کاربر در دیکشنری اضافه بشه برای بررسی های بعدی
            email_dict[self.email]= True
            username_dict[self.username] = True

            print("Registration was successful.")
            
            
            break


    def Login(self) :
        print("\n*Login*")
        while True :
            self.username = input("Username :")
            
            self.password = input("Password :")
            #باید بررسی کنیم که آیا کاربری وجود دارد یا نه
            karbar = None
            #درست بودن یوزر نیم و پسورد را بررسی میکنیم
            for user in self.Users :
                if user.username == self.username and user.password == self.password :
                    karbar = user
                    break
            if karbar is not None :
                print("Login successful! Welcome!")
                break
            else :
                print("The username or password is incorrect. Please try again.")

        self.Users = {'Name' : self.name , 'Email' : self.email , 'Username' : self.username , 'Password' : self.password}
        self.Users.append(self.Users)

        while True :
            select_user = input("Please choose one of these two options : 1. Back to the Menu , \n2.Buy_Ticket")
            if select_user == "Back to the Menu" :
                break
            elif select_user == "Buy_Ticket" :
                print("Welcome to the Buy_Ticket Panel")
                

    def Menu(self):
        while True : #تا زمانی که دکمه بازگشت نخوره این حلقه ادامه داره
            print("Register , \nLogin , \nBack")
            user_choice = input() #کاربر باید از بین 3 گزینه منو یکی را انتخاب کنه
            if user_choice == "Register" :
                Register()
            elif user_choice == "Login" :
                Login()
            elif user_choice == "Back" :
                break
            