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
            print("\n--- Add a new line---")
            print("1. define new line")
            print("2.Return to the employee menu"")
            choice = input(" choose: ")


            if choice == "1":
                self.line_name = input("Enter the name of the new line:")

                if self.line_name in self.lines:
                    print("There is another line with this name. Please enter another name.")
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
                    station_name = input(f"station name : ")
                    self.list_lines.append(station_name)


                #total_distance = 0
                    for i in range(len(self.list_lines) - 1):
                        while True:
                            try:
                                dist = float(input(f" distatnce between count '{self.list_lines[i]}' و '{self.list_lines[i+1]}' (kiliomatier): "))
                                if dist < 0:
                                    print("The distance cannot be negative. Please enter again.")
                                    continue
                                self.total += dist
                                break
                            except ValueError:
                                print("Please enter an integer or decimal number.")

                    print(f"Soft total passed: {self.total} kilometer ")

                dict_ =dict(line_name=self.line_name, start=self.start, end=self.end, total=self.total , Count=self.Count)
                self.line_details.append(dict_)
                print(f"line  '{self.line_name}' Successfully registered.")

            elif choice == "2":
                print("Return to the employee menu.")
                break
            else:
                print("Invalid option! Please try again.")



    def update_line(self):
         while True:
            print("\n--- Line editing---")
            print("1. line edite")
            print("2. Return to the employee menu")
            choice = input( " choose pls " )

            if choice == "1":
                self.line_name = input("Name of the line to edit:")

                if self.line_name not in self.lines:
                    print("There is no line with this name. Please enter a valid name.")
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
                print("\nWhich feature do you want to edit?")
                print("1. stArt")
                print("2. end ")
                print("3. stations")
                feature_choice = input (" your choose :")

                if feature_choice == "1":
                    new_start = input("New origin station name:")
                    for i in self.line_details:
                        if i["line_name"] == self.line_name:
                            i.update({"start":new_start})


                elif feature_choice == "2":
                    new_end = input("New origin station name:")

                    for i in self.line_details:
                        if i["line_name"] == self.line_name:
                            i.update({"end":new_end})
                elif feature_choice == "3":
                    try:
                        self.Count = int(input("Number of stations (excluding origin and destination):"))
                    except ValueError:
                        print("Please enter a valid number.")
                        continue

                    for i in self.line_details:
                        if i["line_name"] == self.line_name:
                            i.update({"Count":self.Count})

                else:
                    print("Invalid option")
            elif choice == "2":
                    print("Return to the employee menu.")
                    break
            else:
                    print("Invalid option! Please try again.")


    def delete_line(self):
         while True:
            print("\n----  delet line  ---")
            print("1. delet line")
            print("2. return to emploee menu")
            choice = input (" choose pls : ")

            if choice == "1":
                line_name = input("The name of the line you want to delete:")

                if line_name not in self.lines:
                    print("There is no line with this name! Please enter the correct name.")
                    continue

                for i in self.line_details:
                    if i["line_name"] == self.line_name:
                        del self.line_details[i]

            elif choice == "2":
                print("return to emploee menu")
                break
            else:
                print("Invalid option! Please try again.")

    def list_line(self):
         while True:
            print("\n--  delet line ---")
            print("1.   delete line ")
            print ("2. return to  ")
            choice = input("your choose  ")

            if choice == "1":
                line_name = input("The name of the line you want to delete:")

                if line_name not in self.lines:
                    print("There is no line with this name! Please enter the correct name.")
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
                print("returen to employee menu")
                break
            else:
                print("Invalid option! Please try again.")
