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



    def add_line(self):
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

                self.start = input("نام ایستگاه مبدا را وارد کنید: ")
                self.end = input("نام ایستگاه مقصد را وارد کنید: ")

                try:
                    self.count = int(input("تعداد ایستگاه‌ها (به جز مبدا و مقصد): "))
                except ValueError:
                    print("لطفاً یک عدد صحیح وارد کنید.")
                    continue
                if self.count <= 0:
                    print("عدد باید بزرگتر از صفر باشد. لطفاً دوباره وارد کنید.")
                    continue
                
                self.list_line = []
                for i in range(self.count):
                    station_name = input(f"نام ایستگاه {i+1}: ")
                    self.list_line.append(station_name)


                total_distance = 0
                    for i in range(len(self.list_line) - 1):
                        while True:
                            try:
                                dist = float(input(f"فاصله بین ایستگاه '{self.list_line[i]}' و '{self.list_line[i+1]}' (کیلومتر): "))
                                if dist < 0:
                                    print("فاصله نمی‌تواند منفی باشد. دوباره وارد کنید.")
                                    continue
                                total_distance += dist
                                break
                            except ValueError:
                                print("لطفا عدد صحیح یا اعشاری وارد کنید.")
                    print(f"مسافت کل طی شده: {total_distance} کیلومتر")
                self.lines[self.line_name] = {
                    'مبدا': self.start,
                    'مقصد': self.end,
                    'ایستگاه‌ها': self.list_line
                }

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

                line_info = self.lines[self.line_name]
                print(f"\nاطلاعات خط '{self.line_name}':")
                print(f"مبدا: {line_info['start']}")
                print(f"مقصد: {line_info['end']}")
                print(f"ایستگاه‌ها: {', '.join(line_info['ایستگاه‌ها'])}")

                print("\nکدام ویژگی را می‌خواهید ویرایش کنید؟")
                print("1. مبدا")
                print("2. مقصد")
                print("3. ایستگاه‌ها")
                feature_choice = input("انتخاب شما: ")

                if feature_choice == "1":
                    new_start = input("نام ایستگاه مبدأ جدید: ")
                    self.lines[self.line_name]['start'] = new_start
                    print("مبدأ با موفقیت ویرایش شد!")

                elif feature_choice == "2":
                    new_end = input("نام ایستگاه مقصد جدید: ")
                    self.lines[self.line_name]['end'] = new_end
                    print("مقصد با موفقیت ویرایش شد!")
                              elif feature_choice == "3":
                    try:
                        self.count = int(input("تعداد ایستگاه‌ها (به جز مبدأ و مقصد): "))
                    except ValueError:
                        print("لطفاً یک عدد صحیح وارد کنید.")
                        continue

                    new_line = []
                    for i in range(self.count):
                        station_name = input(f"نام ایستگاه {i+1}: ")
                        new_line.append(station_name)

                    self.lines[self.line_name]['ایستگاه‌ها'] = new_line
                    print("لیست ایستگاه‌ها با موفقیت ویرایش شد!")

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

                del self.lines[line_name]
                print(f"خط '{line_name}' با موفقیت حذف شد!")

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

                del self.lines[line_name]
                print(f"خط '{line_name}' با موفقیت حذف شد!")

            elif choice == "2":
                print("بازگشت به منوی کارمند.")
                break
            else:
                print("گزینه نامعتبر! لطفاً دوباره تلاش کنید.")
