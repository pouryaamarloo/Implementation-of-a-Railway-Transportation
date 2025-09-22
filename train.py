from logging import exception
import pyinputplus as pyip

class Employee():
    def __init__(self):
        self.line_name = ""
        self.start = ""
        self.end = ""
        self.total = 0
        self.Count = 0
        self.list_lines = []
        self.lines = []
        self.line_details = []


    def add_line(self):

        def check_int(num):
            while True :
                try:
                    num = int(input(num))
                    if num < 0 :
                        print("Please enter a possitive number")
                        continue
                except:
                    print("please enter a number")
                    continue
                return num
        def chek_str():
            while True :
                STR=input()
                if STR == "0":
                    pass
                if STR.isdigit() :
                    continue
                else :
                    return STR



        while True:
            print("\n--- افزودن خط جدید ---")
            print("1. تعریف خط جدید")
            print("2. بازگشت به منوی کارمند")
            choice = input("انتخاب کنید: ")


            if choice == "1":
                self.line_name = input("نام خط جدید رو وارد کنید: ")

                if self.line_name in self.lines:
                    print("خطی دیگر با این نام وجود دارد. لطفا نام دیگری وارد کنید.")
                    continue
                else:
                    self.lines.append(self.line_name)
                print("please enter start")
                self.start = chek_str()
                print("please enter end")
                self.end = chek_str()

                print("please enter Counter of station")
                self.Count = check_int(self.end)
                for i in range(self.Count):
                    station_name = input(f"نام ایستگاه : ")
                    self.list_lines.append(station_name)


                #total_distance = 0
                    for i in range(len(self.list_lines) - 1):
                        while True:
                            try:
                                dist = float(input(f"فاصله بین ایستگاه '{self.list_lines[i]}' و '{self.list_lines[i+1]}' (کیلومتر): "))
                                if dist < 0:
                                    print("فاصله نمی‌تواند منفی باشد. دوباره وارد کنید.")
                                    continue
                                self.total += dist
                                break
                            except ValueError:
                                print("لطفا عدد صحیح یا اعشاری وارد کنید.")

                    print(f"مسافت کل طی شده: {self.total} کیلومتر")

                dict_ =dict(line_name=self.line_name, start=self.start, end=self.end, total=self.total , Count=self.Count)
                self.line_details.append(dict_)
                print(f"خط '{self.line_name}' با موفقیت ثبت شد.")

            elif choice == "2":
                print("بازگشت به منوی کارمند.")
                break
            else:
                print("گزینه نامعتبر! لطفاً دوباره تلاش کنید.")



    def update_line(self):
         while True:
            print("\n--- ویرایش خط ---")
            print("1. ویرایش خط")
            print("2. بازگشت به منوی کارمند")
            choice = input("انتخاب کنید: ")

            if choice == "1":
                self.line_name = input("نام خط مورد نظر برای ویرایش: ")

                if self.line_name not in self.lines:
                    print("خطی با این نام موجود نیست. لطفاً نام صحیح وارد کنید.")
                    continue

                for i in self.line_details:
                    if i["line_name"] == self.line_name:
                        f= f"""
                            line_name : {i["line_name"]}
                            start     : {i["start"]}
                            end       : {i["end"]}
                            total     : {i["total"]}
                            Count     : {i["Count"]}
                            """
                        print(f)
                print("\nکدام ویژگی را می‌خواهید ویرایش کنید؟")
                print("1. مبدا")
                print("2. مقصد")
                print("3. ایستگاه‌ها")
                feature_choice = input("انتخاب شما: ")

                if feature_choice == "1":
                    new_start = input("نام ایستگاه مبدأ جدید: ")
                    for i in self.line_details:
                        if i["line_name"] == self.line_name:
                            i.update({"start":new_start})


                elif feature_choice == "2":
                    new_end = input("نام ایستگاه مقصد جدید: ")

                    for i in self.line_details:
                        if i["line_name"] == self.line_name:
                            i.update({"end":new_end})
                elif feature_choice == "3":
                    try:
                        self.Count = int(input("تعداد ایستگاه‌ها (به جز مبدأ و مقصد): "))
                    except ValueError:
                        print("لطفاً یک عدد صحیح وارد کنید.")
                        continue

                    for i in self.line_details:
                        if i["line_name"] == self.line_name:
                            i.update({"Count":self.Count})

                else:
                    print("گزینه نامعتبر!")
            elif choice == "2":
                    print("بازگشت به منوی کارمند.")
                    break
            else:
                    print("گزینه نامعتبر! لطفاً دوباره تلاش کنید.")


    def delete_line(self):
         while True:
            print("\n--- حذف خط ---")
            print("1. حذف خط")
            print("2. بازگشت به منوی کارمند")
            choice = input("انتخاب کنید: ")

            if choice == "1":
                line_name = input("نام خطی که می‌خواهید حذف کنید: ")

                if line_name not in self.lines:
                    print("خطی با این نام وجود ندارد! لطفاً نام صحیح وارد کنید.")
                    continue

                for i in self.line_details:
                    if i["line_name"] == self.line_name:
                        del self.line_details[i]

            elif choice == "2":
                print("بازگشت به منوی کارمند.")
                break
            else:
                print("گزینه نامعتبر! لطفاً دوباره تلاش کنید.")


    def list_line(self):
         while True:
            print("\n--- حذف خط ---")
            print("1. حذف خط")
            print("2. بازگشت به منوی کارمند")
            choice = input("انتخاب کنید: ")

            if choice == "1":
                line_name = input("نام خطی که می‌خواهید حذف کنید: ")

                if line_name not in self.lines:
                    print("خطی با این نام وجود ندارد! لطفاً نام صحیح وارد کنید.")
                    continue

                for i in self.line_details:
                    if i["line_name"] == self.line_name:
                        a = f"""
                            line_name : {i["line_name"]}
                            start     : {i["start"]}
                            end       : {i["end"]}
                            Count     : {i["Count"]}
                            total     : {i["total"]}
                        """
                        print(a)
            elif choice == "2":
                print("بازگشت به منوی کارمند.")
                break
            else:
                print("گزینه نامعتبر! لطفاً دوباره تلاش کنید.")
