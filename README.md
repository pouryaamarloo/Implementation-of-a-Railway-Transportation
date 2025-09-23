# Implementation-of-a-Railway-Transportation

A Python-based Train Management System that allows different user roles (Admin, Train Employee, Passenger) to manage and interact with train schedules, lines, and tickets.

---

## Features Overview

The system provides a Start Panel where users choose their role:

1. Admin  
2. Train Employee  
3. Passenger  
4. Exit  

Each role has a dedicated workflow with role-specific features.

---

## Admin Panel (Option 1)

Login: Admin must use reserved credentials:  
- Username: Train_Admin  
- Password: Pass_Train  

Login Rules:  
- Incorrect credentials prompt an error and require re-entry.  
- Admin can go back to the Start Panel.  

Features:  
1. Add Train Employee  
   - Input: First name, Last name, Email, Username, Password  
   - System checks for duplicate usernames and emails  
   - Option to go back  

2. Delete Train Employee  
   - Remove employee by username  
   - Shows error if username does not exist  
   - Option to go back  

3. View Employee List  
   - Displays all registered train employees  
   - Option to go back  

4. Exit Admin Panel  
   - Logs out and returns to Start Panel  

---

## Train Employee Panel (Option 2)

Login: Employees use credentials created by the Admin.  

Features:  

1. Add Line  
   - Input: Line name, Origin, Destination, Number of stations, List of station names  
   - Line names must be unique  
   - Option to go back  

2. Update Line  
   - Modify existing line details  
   - Error shown if line does not exist  
   - Option to go back  

3. Delete Line  
   - Remove line by name  
   - Error if line does not exist  
   - Option to go back  

4. View Line List  
   - Shows all registered lines  
   - Option to go back  

5. Add Train  
   - Input: Train name, Assigned line, Average speed, Station stops, Quality grade, Ticket cost, Capacity  
   - Each train has a unique ID  
   - Option to go back  

6. Delete Train  
   - Remove train by ID  
   - Error if ID does not exist  
   - Option to go back  

7. View Train List  
   - Displays all registered trains  
   - Option to go back  

8. Exit Employee Panel  
   - Logs out and returns to Start Panel  

---

## Passenger Panel (Option 3)

Initial Options:  
1. Register  
   - Input: Name, Email, Username, Password  
   - Checks for uniqueness  
   - Option to go back  

2. Login  
   - Input: Username, Password  
   - Error shown if incorrect  
   - Option to go back  

Ticket Purchase Panel Features:  
1. Search & View Available Trains & Routes  
   - Browse lines, trains, destinations, capacity, ticket prices  

2. Purchase Ticket  
   - Select train and number of tickets  
   - System checks seat availability  
   - Ticket details saved in a text file  

3. View & Update Profile  
   - Update personal details (except username)  
   - Option to go back  

4. Logout  
   - Returns to Passenger Panel  

---

## Exit (Option 4)

Exits the program with a farewell message.
=======
>>>>>>> 1c92b85 (finally)
