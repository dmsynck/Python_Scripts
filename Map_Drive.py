#!/usr/bin/env python3

# Filename: Map_Drive.py
# Purpose: Python script to map a drive letter to a UNC path
# Last file change: 02 November, 2017

import subprocess

def Get_Username():

    user_name = input("Please enter your username:")

    return user_name

def Get_Password():

    password = input("Please enter your password:")

    return password

def Set_Map_Command():

    drive_letter = input("Please enter the drive letter you would like to use: i.e. 'X:', 'Z':, etc \n")
    server = input("Please enter the server name: i.e. 'server_name' \n")
    share = input("Please enter the share name i.e. 'share_name' \n")
    domain = input("Please enter the name of your domain: i.e. 'domain_name' \n")

    map_cmd = "NET USE " + drive_letter + " " + "/USER:" + domain + "\\" + username_01 + " " + "\\\\" + server + "\\" + share + " " + password_01 + " " + "/PERSISTENT:NO"

    print(map_cmd)

    return map_cmd

def Map_Drive(map_var):

    subprocess.run(map_var, stdout=subprocess.PIPE, shell=True)

    return None

username_01 = Get_Username()
print(username_01)
password_01 = Get_Password()
print(password_01)
map_cmd_01 = Set_Map_Command()
print(map_cmd_01)
Map_Drive(map_cmd_01)
