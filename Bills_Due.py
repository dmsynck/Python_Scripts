# Filename: Bills_Due.py
# Purpose: A small python utility to help with managing bills and due dates

# Changelog:
#   *** 3/28/2017 - Initial coding of functions ***
#       added "Display_User_Menu" function            
#       added "Add_Payee" function
#   *** 3/30/2017 - Finished "Add_Payee" function and tested creation of "Payees.txt" file ***

# Import any needed modules
import sys
import os
import time

# Function definitions 

def Display_User_Menu():

    # Display a list of user options

    print("""\n \t \t User Menu: Please choose an option \n \n
             \t 1. Add a bill \n
             \t 2. Add a payee \n
             \t 3. List upcoming bills \n
             \t 4. Get a reminder of upcoming bills \n
             \t 5. Mark a bill as paid \n
             \t 6  Clear the screen \n
             \t 7. Exit program \n \n """)

    user_choice = input("\t \t Please enter a choice: (by number) \n")

    return user_choice

def Add_Bill():

    bill_info = []

    company = input("Please enter the company name \n")
    amount_due = input("Please enter the amount due \n")
    due_date = input("Please enter the due date \n")

    f = open("Payees.txt", "r")
    companies = f.readlines()

    f.close

    for item in companies:
        print("Checking list of company names \n")
        if item == company:
            print("Company name already in list. \n")
#            pass
        else:
            print("Company name not found in list. Please re-run app and select option # 2 'Add a payee' \n")

#        print(item)

def Add_Payee():

    company = input("Please enter the payee / company name \n")
    payees.append(company)

    return payees

payees = []
companies = []

os.system("cls")

menu = 1

while menu:

    menu_option = Display_User_Menu()

    if menu_option == "1":
        print("You chose # 1 \n")
        Add_Bill()
    elif menu_option == "2":
        print("You chose # 2 \n")
        companies = Add_Payee()
        print(companies)
    elif menu_option == "3":
        print("You chose # 3 \n")
    elif menu_option == "4":
        print("You chose # 4 \n")
    elif menu_option == "5":
        print("You chose # 5 \n")
    elif menu_option == "6":
        print("You chose # 6 \n")
        time.sleep(5)
        os.system("cls")
    elif menu_option == "7":
        menu = 0
        print("You chose # 7 \n")
        time.sleep(5)
        os.system("exit")
    else:
        print("Invalid option selected \n")
        print("You must choose from options 1 - 7 \n")
        time.sleep(5)
        menu_option = Display_User_Menu() 

f = open("Payees.txt", "w")

for item in companies:
    f.write(item + "\n")

f.close
