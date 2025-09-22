import re

class ManagementPanel: #Management panel class
    def __init__(self):
        self.employees = []   #List of employees

    def add_employee(self):#Method to add train employee
        while True:
            while True:#Ring to get username
                username = input("Enter username: ").strip() ##The username is entered and the extra space is removed.
                if any(emp["username"] == username for emp in self.employees):#This function is used to check whether an email exists or not.
                    print("Error: Username already exists")#If it is duplicate, an error message is printed and the process continues.
                    continue_choice = self.retry_or_return()
                    if continue_choice == "return":
                        return
                    #If the user selects back, return
                    else:#Otherwise, the loop continues
                        continue
                break
        
            while True:#Password loop
                password = input("Enter password: ").strip()#The password is entered and the extra space is removed.
                if not re.match(r'^[A-Za-z0-9@&]{6,16}$', password):# Using regex, it is checked that the password contains English letters, numbers, @ or & and is between 6 and 16 characters long.
                    print("Password must include letters, numbers, @ or & and length 6-16")# In case of error, the message is printed.
                    continue_choice = self.retry_or_return()
                    if continue_choice == "return":
                        return
                    #If the user selects back, return
   
                    else:#:#Otherwise, the loop continues
                        continue
                break

       
            while True:# loop for getting email
                email = input("Enter email: ").strip()#The email is entered and the extra space is removed.
                if any(emp["email"] == email for emp in self.employees):# It is checked whether the email has a password or not.
                    print("Error: Email already exists")
                    continue
                if not re.match(r'^[a-zA-Z0-9_.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):# Using email, it checks whether the email is one of the two opposite formats.gmail/yahoo
                    print("Email must be in correct format")#If there is an error, an error message will be printed.
                    continue_choice = self.retry_or_return()
                    if continue_choice == "return":# again ask return icon 
                        return
                    else:#Otherwise, continue.
                        continue
                break

        
            while True:#loop for get first and last name 
                name = input("Enter name: ").strip()#The name is entered and the extra space is removed.
                family = input("Enter family: ").strip()#The last name is entered and the extra space is removed.
                if not name.isalpha() or not family.isalpha():#بررسی میکند که فقط حروف وارد شده باشد
                    print("Name and family must only contain letters")
                    continue_choice = self.retry_or_return()
                    if continue_choice == "return":#If it was a mistake, the same rollback procedure will apply.
                        return
                    else:
                        continue
                break
## Add employee to the list
            emp = {
                "username": username,
                "password": password,
                "email": email,
                "name": name,
                "family": family
            }
            ##After entering all the correct information, a dictionary is created that holds the employee information.
            self.employees.append(emp)#The created dictionary is added to the employee list.
            print(f"Employee {username} added successfully.")#The message indicating that the employee was successfully added will be displayed.
                
            repeat=input("Do you want to add another user? \n1: Yes \n2: No\n").strip()
            if repeat == "1":
                continue    
            elif repeat == "2":
                return
            else:
                print("Invalid choice, plaese Choose 1 or 2")
                



    def retry_or_return(self):#Helper method for exiting or retrying
        while True:
            try:
                choice = int(input("1: retry  2: return to panel: "))##Choosing 1 means trying again and 2 means returning to the main panel
                if choice == 1:
                    return "retry"
                elif choice == 2:
                    return "return"
                else:
                    print("Choose 1 or 2")#If a number other than 1 or 2 is entered, it will be requested to be 1 or 2.
            except ValueError:#If the input is not numeric, an exception is thrown and a request is made to enter a number.
                print("Invalid input! Enter a number.")

    def remove_employee(self):#Enters the Add Employee panel. 
        username = input("Enter username to remove: ").strip()#Getting the username to delete an employee and removing the extra space
        for emp in self.employees:
            if emp["username"] == username:#If the entered username exists, the entered username exists.
                self.employees.remove(emp)#The employee is removed
                print(f"Employee {username} removed successfully.")#A deletion success message is printed.
                return
        print("Error: Employee not found!")#If the username is not found, a message will be displayed.

    def list_employees(self):#Method to display all employees
            if not self.employees:# if list empty
            print("No employees found.")# The message will be displayed
        for emp in self.employees:#Otherwise, each employee's information will be printed.
            print(f"Username: {emp['username']}, Name: {emp['name']} {emp['family']}, Email: {emp['email']}")

    def panel(self):  # Otherwise, each employee's information will be printed.
        while True:
            print("\n1: Add employee\n2: Remove employee\n3: Show employees\n4: Exit") 
            choice = input("Choose option: ").strip()#The input is integers between 1 and 4.

            if choice == "1":
                self.add_employee()#Enters the Add Employee panel.

            elif choice == "2":
                self.remove_employee()#Enters the employee deletion panel.

            elif choice == "3":
                self.list_employees()#Enters the Add List panel.

            elif choice == "4":
                print("Exiting panel...")#Exits the entire admin panel.
                return
            
            else:
                print("Invalid choice, enter 1-4")# If you enter integers other than 1 to 4, you will be asked to enter a number between these.