#!/usr/bin/env python3

# Filename: Channel_Lookup.py
# Purpose: To enable lookup of LanSchool channels from a .csv file

import sys
import os
import csv

campus_list = []
campus_dict = {}
channel_list = []

def Build_Campus_List():

    """
    Dynamically build the list of campus names
    """

    list_1 = []

    channel_file = "LanSchool_Combined.csv"

    with open(channel_file, "r") as f:
        reader = csv.reader(f)

        for row in reader:

            if row[0] not in list_1:
                list_1.append(row[0])
            else:
                pass

    f.close()

    return list_1

def Build_Campus_Dict(arg_a):

    """
    Build a dictionary from the campus list we built earlier.
    This is necessary so that we can map a sequence of numbers
    to actual campus designations
    """

    i = 0
    j = " "

    dict_1 = {i: j for i,j in enumerate(arg_a)}

    return dict_1

def Get_Campus(arg_a):

    os.system("clear")

    for k, v in arg_a.items():
        print(k, v)

    choice = input("Please select a campus: 'by number' \n")

    choice = int(choice)

    if choice in arg_a:
        choice = str(arg_a[choice])

    return choice

def Get_Channel(arg_a):

    """
    Get channel information based on user input
    """

    list_1 = []
    chan = " "

    room_cart = input("Please enter the room or cart number \n")
    print()
    print("You entered: " + room_cart + "\n")

    channel_file = "LanSchool_Combined.csv"

    with open(channel_file, "r") as f:
        reader = csv.reader(f)

        for row in reader:
            if arg_a == row[0]:
                list_1.append(row)
            else:
                pass

    f.close()

    for i in list_1:
        print(i)
        if room_cart in i:
            print("Found room or cart: " + room_cart + "\n")
            chan = i[2]
        else:
            pass

    return chan

def main():

    """
    Because every program should have a 'main' function
    """

    campus_list = Build_Campus_List()
    campus_dict = Build_Campus_Dict(campus_list)
    campus = Get_Campus(campus_dict)
    print()
    print("You selected campus: " + campus + "\n")
    channel = Get_Channel(campus)
    print()
    print("Your LanSchool channel number is: " + channel + "\n")

    return None

    sys.exit()

if __name__=="__main__":
    main()
