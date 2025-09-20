import re #چون باید باید از Regex استفاده بشه

class Normal_User_Panel():
    def __init__(self , name , email , username , password):
        self.name = name
        self.email = email
        self.username = username
        self.password = password

        Users = {} #برای ذخیره کردن کاربر
    #باید قبل از گرفتن اطلاعات با ریجکس ایمیل و یوزرنیم و پسورد رو بررسی کنیم
    def Acceptable_Email(email) :
        patern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        correct_email = re.match(patern , email)
        return correct_email
    def Acceptable_Password(password) :
        patern = r'^(?=.*[a-zA-z])(?=.*\d)(?=.*[@&])'
        correct_pass = re.match(patern , password)
        return correct_pass
    def Acceptable_Username(username)